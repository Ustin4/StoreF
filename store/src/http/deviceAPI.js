import {$authHost, $host} from "./API";

export const createType = async (type) => {
    const {data} = await $authHost.post('api/type/', type + '?format=json')
    return data
}

export const fetchTypes = async () => {
    const {data} = await $host.get('api/type/?format=json')
    return data
}

export const createBrand = async (brand) => {
    const {data} = await $authHost.post('api/brand/', brand + '?format=json')
    return data
}

export const fetchBrands = async () => {
    const {data} = await $host.get('api/brand/?format=json', )
    return data
}

export const createDevice = async (device) => {
    const {data} = await $authHost.post('api/device/', device + '?format=json')
    return data
}

export const fetchDevices = async (typeId, brandId, page, limit= 5) => {
    const {data} = await $host.get('api/device/?format=json', {params: {
            typeId, brandId, page, limit
        }})
    return data
}

export const fetchOneDevice = async (id) => {
    const {data} = await $host.get(`api/device/${id}/?format=json`)
    return data
}
