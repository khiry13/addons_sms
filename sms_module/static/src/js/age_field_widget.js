/** @odoo-module **/

import {registry} from "@web/core/registry";
import {_t} from "@web/core/l10n/translation";
import {useRecordObserver} from "@web/model/relational_model/utils";
import {standardFieldProps} from "@web/views/fields/standard_field_props";
import {Component, useState, useEffect, onWillUpdateProps} from "@odoo/owl";


const {DateTime} = luxon;

export class AgeWidget extends Component {
    static template = "sms_module.AgeWidget";

    static props = {
        ...standardFieldProps,
        is_month: {type: Boolean, optional: true}, // Prop to include months
        is_day: {type: Boolean, optional: true}, // Prop to include days
    };

    static defaultProps = {
        ...standardFieldProps.defaultProps,
        is_month: true,
        is_day: false,  // Default to false if not provided
    };

    get formattedAge() {
        console.log("AgeWidget >> formattedAge :",);
        const dob = this.props.record.data[this.props.name];
        if (dob) {
            console.log("AgeWidget >> useEffect , dob changed:", dob);
            this.state.age = this.calculateAge(dob);
        }
        return this.state.age;
    }

    setup() {
        console.log("AgeWidget >> setup , this.props:", this.props);


        this.state = useState({
            age: this.calculateAge(this.props.record.data[this.props.name]),
        });

        console.log("AgeWidget >> setup , this.state:", this.state);


        // useRecordObserver( (record) => {
        //         console.log("AgeWidget >> useRecordObserver , record:", record);
        //         const dob = record.data[this.props.name];
        //         this.state.age = this.calculateAge(dob);
        //
        // })

        // Add a watcher or useEffect to monitor changes in dob and recalculate the age
        // useEffect(() => {
        //     const dob = this.props.record.data[this.props.name];
        //     if (dob) {
        //         console.log("AgeWidget >> useEffect , dob changed:", dob);
        //         this.state.age = this.calculateAge(dob);
        //     }
        // }, () => [this.props.record.data[this.props.name]]); // Observe changes to the dob prop


    }

    /**
     * Calculate age based on the date of birth and props.
     */
    calculateAge(dob) {
        const dobDate = DateTime.fromISO(dob);
        const now = DateTime.now();
        let age = now.diff(dobDate, ['years', 'months', 'days']).toObject();

        let ageString = `${Math.floor(age.years)} ${_t("years")}`;
        if (this.props.is_month) {
            ageString += `, ${Math.floor(age.months)} ${_t("months")}`;
        }
        if (this.props.is_day) {
            ageString += `, ${Math.floor(age.days)} ${_t("days")}`;
        }
        console.log("AgeWidget >> calculateAge , ageString:", ageString);
        return ageString;

    }
}


// export the widget for usage in other modules
export const ageWidgetField = {
    component: AgeWidget,
    supportedTypes: ["date"],
};


// Register the widget in the registry
registry.category("fields").add("AgeWidget", ageWidgetField);