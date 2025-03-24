/** @odoo-module **/

import { Component, onWillStart, useState, onWillDestroy } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";


export class DashboardCountItem extends Component {
    static template = "sms_module.DashboardCountItem";
    static props = {
        size: {
            type: Number,
            optional: true
        },
        color: {
            type: String,
            optional: true
        },
        main_icon: {
            type: String,
            optional: true
        },
        chart_icon: {
            type: String,
            optional: true
        },
        label: {
            type: String,
            optional: true
        },
        model: {
            type: String,
            optional: true
        },
        domain: {
            type: Array,
            optional: true
        }
    }

    static defaultProps = {
        size: 1,
        color: "bg-success",
        main_icon: "fa-user",
        chart_icon: "fa-bar-chart",
        label: "Students",
        model: "sms_module.student",
        domain: []
    }

    setup() {

        console.log("this.props: ", this.props)
        this.action = useService("action");
        this.orm = useService("orm")
        this.busService = this.env.services.bus_service;

        // State to store dashboard data
        this.state = useState({
            count: 0
        });

        onWillStart(this.onWillStart)

        const refreshBusListener = (payload) => {
            if (payload.model === this.props.model) {
                this.fetchData();
            }
        }
        this.busService.subscribe('auto_refresh', refreshBusListener);
        this.busService.addChannel('auto_refresh');
        this._refreshStopBus = () => {
            this.busService.unsubscribe('auto_refresh', refreshBusListener);
            this.busService.deleteChannel('auto_refresh');
        }

        onWillDestroy(() => {
            this._refreshStopBus();
        });
//        console.log("auto refresh >> patch ListController >> setup");
//        this.env.services.bus_service.addChannel('auto_refresh')
//        const listenerRef = this.env.services.bus_service.addEventListener('notification', ({detail: notifications}) => {
//            console.log("DashboardCountItem >> Notification received: ", notifications);
//            for (const {payload, type} of notifications) {
//                if (type === 'auto_refresh' && payload.model === this.props.model) {
//                    this.fetchData()
//                }
//            }
//        })
//
//        this.env.services.bus_service.start();
//
//        onWillDestroy(() => {
//            console.log("auto refresh >> DashboardCountItem >> onWillDestroy");
//            this.env.bus.removeEventListener("notification", listenerRef)
//            this.env.services.bus_service.stop();
//        });


    }

    async onWillStart() {
        await this.fetchData()
    }


    async fetchData() {
        await this.orm.searchCount(this.props.model, this.props.domain).then(result => {
            console.log("result: ", result);
            this.state.count = result;
        })

    }

    get count() {
        return this.state.count;
    }

    showMore() {
        this.action.doAction(`${this.props.model}_action`)
    }

}

