import axios from "axios"

export const getHelloWorld = async () => {
  const { data } = await axios.get("http://localhost:8000/hello_world")
  return data
}
