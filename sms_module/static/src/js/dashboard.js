/** @odoo-module **/

import { Component, onWillStart, useState } from "@odoo/owl";
import {DashboardCountItem} from "./dashboard_count_item";
import { registry } from "@web/core/registry";
//import {jsonrpc} from "@web/core/network/rpc_service";
import { useService } from "@web/core/utils/hooks";


export class Dashboard extends Component {
    static template = "sms_module.DashboardTemplate";
    static components = {DashboardCountItem}

    setup() {
        this.action = useService("action");
        this.orm = useService("orm");
        // State to store dashboard data
//        this.state = useState({
//            userCount: 0,
//            student_count: 0,
//            alertsCount: 0,
//            ordersCount: 0,
//        });

//        onWillStart(this.onWillStart)
    }

//    async onWillStart() {
//        await this.fetchData();
//    }
//
//    async fetchData() {
//        // Fetch user count
//        const userCount = await this.orm.searchCount("res.users", []);
//
//        // Fetch student count
//        const studentCount = await this.orm.searchCount("sms_module.student", []);
//
//        // Fetch alerts count
//        const alertsCount = await this.orm.searchCount("mail.activity", []);
//
//        // Fetch orders count
//        const ordersCount = await this.orm.searchCount("sale.order", []);
//
//        console.log("data", studentCount)
//
//        // Update state with fetched counts
//        this.state.userCount = userCount;
//        this.state.studentCount = studentCount;
//        this.state.alertsCount = alertsCount;
//        this.state.ordersCount = ordersCount;
//        var self = this;
//
//        const response = jsonrpc("/sms_module/dashboard/data", {}).then(function(data_result) {
//            self.state.userCount = data_result.user_count;
//            self.state.student_count = data_result.student_count;
//            self.state.alertsCount = data_result.alerts_count;
//            self.state.ordersCount = data_result.orders_count;
//        })

//    }

    openUsers() {
        this.action.doAction({
            type: "ir.actions.act_window",
            name: "All users",
            res_model: "res.users",
            views: [
                [false, "list"],
                [false, "form"],
            ],
        });
    }

    openStudents() {
        this.action.doAction({
            type: "ir.actions.act_window",
            name: "All students",
            res_model: "sms_module.student",
            views: [
                [false, "list"],
                [false, "form"],
            ],
        });
    }

    openAlerts() {
        this.action.doAction({
            type: "ir.actions.act_window",
            name: "All alerts",
            res_model: "mail.activity",
            views: [
                [false, "list"],
                [false, "form"],
            ],
        });
    }

    openOrders() {
        this.action.doAction({
            type: "ir.actions.act_window",
            name: "All orders",
            res_model: "sale.order",
            views: [
                [false, "list"],
                [false, "form"],
            ],
        });
    }

}

registry.category("actions").add("sms_dashboard", Dashboard);

