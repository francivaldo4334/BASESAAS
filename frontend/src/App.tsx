import { defineComponent } from "vue";
import { useGetHelloWorld } from "./queries/useGetHelloWorld";

export default defineComponent({
  setup() {
    const query = useGetHelloWorld()
    return { query }
  },
  computed: {
    items(): {
      id: number,
      title: string,
      description: string,
      slug: string
    }[] {
      return this.query.data.value || []
    }
  },
  render() {
    return (
      <>
        <ul class="list">
          {this.items.map(obj => (
            <li class="list-row">
              <div>{obj.title}</div>
              <div>{obj.description}</div>
            </li>
          ))}
        </ul>
      </>
    )
  }
})
