Challenge -

1. Using python, CREATE a sqlite table to store the switch configuration in. Create (at least) the following columns:
			- hostname
			- ip
			- startup_config
			- running_config
			- valid_config
			
2. Using python, INSERT known information into the sqlite table (hostname and ip)

3. Using your previous python scripts, retrieve the startup_config and running_config for each switch and update the database (columns startup_config and running_config) with this information.

4. Using your previous python scripts, run the configuration validation check for each switch and update the database (column valid_config [True|False]) with this information.
