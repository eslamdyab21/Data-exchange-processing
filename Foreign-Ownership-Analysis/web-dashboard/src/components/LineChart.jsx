import { ResponsiveLine } from "@nivo/line";
import { useTheme } from "@mui/material";
import { tokens } from "../theme";
import { mockLineData as data } from "../data/mockData";


function convertFormat(filteredLineGraphData){

  let line_data = [{id: "data", 
                  color: tokens("dark").greenAccent[500],
                  data:[]}]

  // for (let i = 0; i < Object.keys(filteredLineGraphData["FO%"]).length; i++) {
  //   line_data['data'].push({'x':filteredLineGraphData["Date"], 'y':filteredLineGraphData["FO%"]})
  // }

  console.log('filteredLineGraphData', filteredLineGraphData)

  for (let i = 0; i < Object.keys(filteredLineGraphData["FO%"]).length; i++) {
    line_data[0]['data'].push({'x':i, 'y':filteredLineGraphData["FO%"][Object.keys(filteredLineGraphData["FO%"])[i]]})
  }

  console.log('Object.keys(filteredLineGraphData["FO%"]).length', Object.keys(filteredLineGraphData["FO%"]).length)
  console.log('line_data', line_data)

  return line_data
}

const LineChart = ({ filteredLineGraphData = [], isCustomLineColors = false, isDashboard = false }) => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);
  let line_data = null

  console.log('len', filteredLineGraphData.length)

  if (filteredLineGraphData.length > 0){
    filteredLineGraphData = JSON.parse(filteredLineGraphData)
    line_data = convertFormat(filteredLineGraphData)
  }


  if (line_data){
      return (
    
    <ResponsiveLine
      data={line_data}
      theme={{
        axis: {
          domain: {
            line: {
              stroke: colors.grey[100],
            },
          },
          legend: {
            text: {
              fill: colors.grey[100],
            },
          },
          ticks: {
            line: {
              stroke: colors.grey[100],
              strokeWidth: 1,
            },
            text: {
              fill: colors.grey[100],
            },
          },
        },
        legends: {
          text: {
            fill: colors.grey[100],
          },
        },
        tooltip: {
          container: {
            color: colors.primary[500],
          },
        },
      }}
      colors={isDashboard ? { datum: "color" } : { scheme: "nivo" }} // added
      margin={{ top: 50, right: 110, bottom: 50, left: 60 }}
      xScale={{ type: "linear" }}
      yScale={{
        type: "linear",
        min: "auto",
        max: "auto",
        stacked: true,
        reverse: false,
      }}
      yFormat=" >-.2f"
      curve="catmullRom"
      axisTop={null}
      axisRight={null}
      axisBottom={{
        orient: "bottom",
        tickSize: 0,
        tickPadding: 5,
        tickRotation: 0,
        legend: isDashboard ? undefined : "transportation", // added
        legendOffset: 36,
        legendPosition: "middle",
      }}
      axisLeft={{
        orient: "left",
        tickValues: 5, // added
        tickSize: 3,
        tickPadding: 5,
        tickRotation: 0,
        legend: isDashboard ? undefined : "count", // added
        legendOffset: -40,
        legendPosition: "middle",
      }}
      enableGridX={false}
      enableGridY={false}
      pointSize={8}
      pointColor={{ theme: "background" }}
      pointBorderWidth={2}
      pointBorderColor={{ from: "serieColor" }}
      pointLabelYOffset={-12}
      useMesh={true}
      legends={[
        {
          anchor: "bottom-right",
          direction: "column",
          justify: false,
          translateX: 100,
          translateY: 0,
          itemsSpacing: 0,
          itemDirection: "left-to-right",
          itemWidth: 80,
          itemHeight: 20,
          itemOpacity: 0.75,
          symbolSize: 12,
          symbolShape: "circle",
          symbolBorderColor: "rgba(0, 0, 0, .5)",
          effects: [
            {
              on: "hover",
              style: {
                itemBackground: "rgba(0, 0, 0, .03)",
                itemOpacity: 1,
              },
            },
          ],
        },
      ]}
    />
  );
  }

};

export default LineChart;
