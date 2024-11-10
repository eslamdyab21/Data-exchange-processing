import axios from 'axios'

const API_BASE_URL = 'http://localhost:8000'

const instance = axios.create({
  baseURL: API_BASE_URL,
  timeout: 10000,
})


const fetchLineGraphSelections = async () => {
  try {
    const response = await instance.get('/line_graph_selections');

    return response.data;

  } catch (error) {
    throw error;
  }
}

const getFilterdLineGraph = async (selections) => {
  try {
    const response = await instance.post(`/line_graph`, { selections })
    
    return response.data;
    
  } catch (error) {
    throw error;
  }
}

export  {fetchLineGraphSelections, getFilterdLineGraph};


