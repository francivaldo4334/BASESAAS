import { getHelloWorld } from "@/services/api/queries"
import { useQuery } from "@tanstack/vue-query"

export const useGetHelloWorld = () => {
  return useQuery({
    queryFn: () => getHelloWorld(),
    queryKey: ["getHelloWorld"]
  })
}
