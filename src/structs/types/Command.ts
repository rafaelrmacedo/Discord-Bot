import { CommandInteraction, CommandInteractionOptionResolver, ButtonInteraction, Collection, StringSelectMenuInteraction, ModalSubmitInteraction, ApplicationCommandData } from "discord.js";
import { ExtendClient } from "../ExtendedClient";

interface CommandProps{
    client: ExtendClient
    interaction: CommandInteraction, 
    options: CommandInteractionOptionResolver
}

export type ComponentsButton = Collection<string, (interaction: ButtonInteraction) => any>
export type ComponentsSelect = Collection<string, (interaction: StringSelectMenuInteraction) => any>
export type ComponentsModal = Collection<string, (interaction: ModalSubmitInteraction) => any>

interface CommandComponents {
    buttons?: ComponentsButton
    selects?: ComponentsSelect
    modals?: ComponentsModal
}

export type CommandType = ApplicationCommandData & CommandComponents & {
    run: (props: CommandProps) => any
}

export class Command {
    constructor(options: CommandType) {
        options.dmPermission = false
        Object.assign(this, options)
    }
}