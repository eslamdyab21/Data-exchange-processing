import { Box } from "@mui/material";
import { DataGrid, GridToolbar } from "@mui/x-data-grid";
import { tokens } from "../theme.js";
import { useTheme } from "@mui/material";
import dayjs from 'dayjs';



const DataTable = (props) => {
  
  let data = []
  let filteredLineGraphData = props.filteredLineGraphData

  if (props.filteredLineGraphData){
    data = filteredLineGraphData
  }


  const theme = useTheme();
  const colors = tokens(theme.palette.mode);

  const columns = [
    { field: "id", 
      headerName: "id", 
      flex: 0.5 
    },
    { field: "Date", 
      headerName: "Date",
      type: "date",
      valueFormatter: (params) => dayjs(params.value).format('YYYY-MM-DD'),
    },
    {
      field: "Ticker",
      headerName: "Ticker",
      flex: 1,
      cellClassName: "name-column--cell",
    },
    {
      field: "FO WTD",
      headerName: "FO WTD",
      type: "number",
      headerAlign: "left",
      align: "left",
    },
    {
      field: "FO MTD",
      headerName: "FO MTD",
      flex: 1,
    },
    {
      field: "FO YTD",
      headerName: "FO YTD",
      flex: 1,
    },
    {
      field: "Foreign Headroom",
      headerName: "Foreign Headroom",
      flex: 1,
    },
    {
      field: "FO%",
      headerName: "FO%",
      flex: 1,
    },
    {
      field: "Country",
      headerName: "Country",
      flex: 1,
    },
    {
      field: "Sector",
      headerName: "Sector",
      flex: 1,
    },
    {
      field: "EXCHANGE",
      headerName: "EXCHANGE",
      flex: 1,
    },
  ];

  if (props.filteredLineGraphData){
   
  return (
    <Box m="20px">
      <Box
        m="40px 0 0 0"
        height="95vh"
        sx={{
          "& .MuiDataGrid-root": {
            border: "none",
          },
          "& .MuiDataGrid-cell": {
            borderBottom: "none",
          },
          "& .name-column--cell": {
            color: colors.greenAccent[300],
          },
          "& .MuiDataGrid-columnHeaders": {
            backgroundColor: colors.blueAccent[700],
            borderBottom: "none",
          },
          "& .MuiDataGrid-virtualScroller": {
            backgroundColor: colors.primary[400],
          },
          "& .MuiDataGrid-footerContainer": {
            borderTop: "none",
            backgroundColor: colors.blueAccent[700],
          },
          "& .MuiCheckbox-root": {
            color: `${colors.greenAccent[200]} !important`,
          },
          "& .MuiDataGrid-toolbarContainer .MuiButton-text": {
            color: `${colors.grey[100]} !important`,
          },
        }}
      >
        <DataGrid
          rows={data}
          columns={columns}
          components={{ Toolbar: GridToolbar }}
        />
      </Box>
    </Box>
  );}
};

export default DataTable;
