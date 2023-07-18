import unittest
import os
from save_to_excel import save_domain_status_to_excel


class TestSaveToExcel(unittest.TestCase):
    def test_save_domain_status_to_excel(self):
        # Sample domain status data
        domain_status_list = [
            ("example.com", "Up and running"),
            ("example-down.com", "Down with status code: 404"),
            ("example-error.com", "Down with an error: Connection refused"),
        ]

        # Save domain status data to Excel
        output_file_path = save_domain_status_to_excel(domain_status_list)

        # Check if the file was created and not empty
        self.assertTrue(os.path.exists(output_file_path))
        self.assertTrue(os.path.getsize(output_file_path) > 0)

        # Clean up: remove the created file
        os.remove(output_file_path)


if __name__ == "__main__":
    unittest.main()
