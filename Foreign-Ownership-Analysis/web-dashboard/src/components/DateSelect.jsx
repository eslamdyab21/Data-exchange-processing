import * as React from 'react';
import { useCallback, useEffect} from "react";
import { DemoContainer } from '@mui/x-date-pickers/internals/demo';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { DatePicker } from '@mui/x-date-pickers/DatePicker';
import dayjs from 'dayjs';



export default function BasicDatePicker(props) {
  const [value, setValue] = React.useState(null);
  const {updateParentSelections} = props;

  useEffect(() => {
    updateParentSelections(props.name, dayjs(value).format('YYYY-MM-DD'))
   }, [value]);



  return (
    <LocalizationProvider dateAdapter={AdapterDayjs}>
      <DemoContainer components={['DatePicker']}>
        <DatePicker 
          label={props.name} 
          // format="YYYY-MM-DD"
          value={value}
          onChange={(newValue) => setValue(newValue)}
        />
      </DemoContainer>
    </LocalizationProvider>
  );
}
