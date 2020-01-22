# Shell script that gets the temperature
# for 1 MCP9808 connected I2C device

ICYPI_DIR='/home/pi/Documents/gitProjects/icypi';
cd $ICYPI_DIR;
source venv/bin/activate;
python src/get_temperature_mcp9808.py;
