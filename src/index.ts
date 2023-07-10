import { ExtendClient } from "./structs/ExtendedClient"
import config from './config.json';
export * from 'colors';

const client = new ExtendClient();

client.start();

export { client, config }