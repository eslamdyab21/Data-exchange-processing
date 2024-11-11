import { Box, Typography, useTheme } from "@mui/material";
import { tokens } from "../../theme";
import EmailIcon from "@mui/icons-material/Email";
import PointOfSaleIcon from "@mui/icons-material/PointOfSale";
import PersonAddIcon from "@mui/icons-material/PersonAdd";
import TrafficIcon from "@mui/icons-material/Traffic";
import LineChart from "../../components/LineChart";
import StatBox from "../../components/StatBox";
import MultipleSelectChip from "../../components/MultiSelect"
import BasicDatePicker from "../../components/DateSelect"
import Button from '@mui/material/Button';
import {fetchLineGraphSelections, getFilterdLineGraph} from '../../api/api';
import {useState, useEffect} from 'react';
import axios from 'axios'




const Dashboard = () => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);
  const [lineGraphSelections, setLineGraphSelections] = useState([]);
  const [loading, setLoading] = useState(true);
  const [filteredLineGraph, setFilteredLineGraph] = useState(null);
  const [buttonClicled, setButtonClicled] = useState(false);

  const [tickersSelection, setTickersSelection] = useState([]);
  const [countriesSelection, setCountriesSelection] = useState([]);
  const [sectorsSelection, setSectorsSelection] = useState([]);
  const [exchangesSelection, setExchangesSelection] = useState([]);
  const [yaxisSelection, setYaxisSelection] = useState(['FO%']);
  const [startDateSelection, setStartDateSelection] = useState([]);
  const [endDateSelection, setEndDateSelection] = useState([]);


  let selections = null

  useEffect(() => {
    fetchLineGraphSelections()
      .then(data => {
        setLineGraphSelections(data);
        setLoading(false);
      })

      .catch(err => {
        console.log(err)
        setLoading(false);
      });

  }, []);


  useEffect(() => {
    selections = {'Tickers':tickersSelection, 'Countries':countriesSelection,
                    'Sectors':sectorsSelection, 'Exchanges':exchangesSelection,
                    'Y-axis': yaxisSelection, 'Start Date': startDateSelection,
                    'End Date': endDateSelection}


    if(buttonClicled){
      setButtonClicled(false)

      getFilterdLineGraph(selections).then(result => {
        setFilteredLineGraph(result)
    });

    }

  }, [buttonClicled]);



  const updateParentSelections = (name, values) => {
    if(name == 'Tickers')
      setTickersSelection(values)
    else if (name == 'Countries')
      setCountriesSelection(values)
    else if (name == 'Sectors')
      setSectorsSelection(values)
    else if (name == 'Exchanges')
      setExchangesSelection(values)
    else if (name == 'Y-axis')
      setYaxisSelection(values)
    else if (name == 'Start Date')
      setStartDateSelection(values)
    else if (name == 'End Date')
      setEndDateSelection(values)

  }


  return (
    <Box m="20px">

      {/* GRID & CHARTS */}
      <Box
        display="grid"
        gridTemplateColumns="repeat(12, 1fr)"
        gridAutoRows="140px"
        gap="1px"
      >
        {/* ROW 1 */}
        <Box
          gridColumn="span 3"
          backgroundColor={colors.primary[400]}
          display="flex"
          alignItems="center"
          justifyContent="center"
        >
          <StatBox
            title="4"
            subtitle="Countries"
            progress="0.75"
            icon={
              <EmailIcon
                sx={{ color: colors.greenAccent[600], fontSize: "26px" }}
              />
            }
          />
        </Box>
        <Box
          gridColumn="span 3"
          backgroundColor={colors.primary[400]}
          display="flex"
          alignItems="center"
          justifyContent="center"
        >
          <StatBox
            title="14"
            subtitle="Sectors"
            progress="0.75"
            icon={
              <PointOfSaleIcon
                sx={{ color: colors.greenAccent[600], fontSize: "26px" }}
              />
            }
          />
        </Box>
        <Box
          gridColumn="span 3"
          backgroundColor={colors.primary[400]}
          display="flex"
          alignItems="center"
          justifyContent="center"
        >
          <StatBox
            title="4"
            subtitle="Exchange places"
            progress="0.75"
            icon={
              <PersonAddIcon
                sx={{ color: colors.greenAccent[600], fontSize: "26px" }}
              />
            }
          />
        </Box>
        <Box
          gridColumn="span 3"
          backgroundColor={colors.primary[400]}
          display="flex"
          alignItems="center"
          justifyContent="center"
        >
          <StatBox
            title="288"
            subtitle="Tickers"
            progress="0.75"
            icon={
              <TrafficIcon
                sx={{ color: colors.greenAccent[600], fontSize: "26px" }}
              />
            }
          />
        </Box>


        {/* ROW 2 */}
        
          <Box
            gridColumn="span 3"
            display="flex"
            alignItems="center"
            justifyContent="center"
          >

            <MultipleSelectChip name={'Tickers'} names={lineGraphSelections.Tickers ?? []} updateParentSelections={updateParentSelections} ></MultipleSelectChip>
          </Box>
          
          <Box
            gridColumn="span 3"
            display="flex"
            alignItems="center"
            justifyContent="center"
          >
            <MultipleSelectChip  name={'Countries'} names={lineGraphSelections.Countries ?? [] } updateParentSelections={updateParentSelections}></MultipleSelectChip>
          </Box>

          <Box
            gridColumn="span 3"
            display="flex"
            alignItems="center"
            justifyContent="center"
          >
            <MultipleSelectChip name={'Sectors'} names={lineGraphSelections.Sectors ?? [] } updateParentSelections={updateParentSelections}></MultipleSelectChip>
          </Box>

          <Box
            gridColumn="span 3"
            display="flex"
            alignItems="center"
            justifyContent="center"
          >
            <MultipleSelectChip name={'Exchange places'} names={lineGraphSelections.Exchanges ?? [] } updateParentSelections={updateParentSelections}></MultipleSelectChip>
          </Box>


          <Box
            gridColumn="span 3"
            display="flex"
            alignItems="center"
            justifyContent="center"
            marginTop='-150px'
          >
            <MultipleSelectChip name={'Y-axis'} names={lineGraphSelections.y_axis ?? [] } updateParentSelections={updateParentSelections}></MultipleSelectChip>
          </Box>

          <Box
            gridColumn="span 3"
            display="flex"
            alignItems="center"
            justifyContent="center"
            marginTop='-150px'
          >
            <BasicDatePicker name={'Start Date'} updateParentSelections={updateParentSelections}></BasicDatePicker>
          </Box>

          <Box
            gridColumn="span 3"
            display="flex"
            alignItems="center"
            justifyContent="center"
            marginTop='-150px'
          >
            <BasicDatePicker name={'End Date'}  updateParentSelections={updateParentSelections}></BasicDatePicker>
          </Box>
          
        {/*<BasicButtons> </BasicButtons>*/}

        {/* ROW 3 */}
        <Box
          gridColumn="span 12"
          gridRow="span 3"
          backgroundColor={colors.primary[400]}
          marginTop='-100px'
        >

        <Box
            mt="25px"
            p="0 30px"
            display="flex "
            justifyContent="space-between"
            alignItems="center"
          >
            <Box>
              <Typography
                variant="h5"
                fontWeight="600"
                color={colors.grey[100]}
              >
                Statstics
              </Typography>
              <Typography
                variant="h3"
                fontWeight="bold"
                color={colors.greenAccent[500]}
              >
              </Typography>
            </Box>
            <Box>
              <Button 
                  onClick={() => { setButtonClicled(true)}}
                  variant="contained">Plot
              </Button>
            </Box>
          </Box>
          <Box
            mt="25px"
            p="0 30px"
            display="flex "
            justifyContent="space-between"
            alignItems="center"
          >
            <Box>
              <Typography
                variant="h5"
                fontWeight="600"
                color={colors.grey[100]}
              >
                Line chart
              </Typography>
            </Box>
            <Box>
            </Box>
          </Box>
          <Box height="400px" m="-20px 0 0 0">
            <LineChart filteredLineGraphData = {filteredLineGraph ?? []} y_axis = {yaxisSelection ?? null} isDashboard={true} />
          </Box>
        </Box>


      </Box>
    </Box>
  );
};

export default Dashboard;
