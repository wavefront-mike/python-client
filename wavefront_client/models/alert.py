# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class Alert(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Alert - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'active_maintenance_windows': 'list[str]',
            'additional_information': 'str',
            'condition': 'str',
            'condition_qb_enabled': 'bool',
            'condition_qb_serialization': 'str',
            'created': 'int',
            'display_expression': 'str',
            'display_expression_qb_enabled': 'bool',
            'display_expression_qb_serialization': 'str',
            'event': 'ReportEvent',
            'failing_host_label_pairs_override': 'list[HostLabelPair]',
            'hosts_used': 'list[str]',
            'in_maintenance_host_label_pairs': 'list[HostLabelPair]',
            'in_trash': 'bool',
            'last_error_message': 'str',
            'last_failed_time': 'int',
            'last_updated': 'int',
            'metrics_used': 'list[str]',
            'minutes': 'int',
            'name': 'str',
            'notificants': 'list[str]',
            'prefiring_host_label_pairs': 'list[HostLabelPair]',
            'query_failing': 'bool',
            'resolve_after_minutes': 'int',
            'severity': 'str',
            'snoozed': 'int',
            'tags': 'Tags',
            'target': 'str',
            'update_user_id': 'str',
            'updated': 'int'
        }

        self.attribute_map = {
            'active_maintenance_windows': 'activeMaintenanceWindows',
            'additional_information': 'additionalInformation',
            'condition': 'condition',
            'condition_qb_enabled': 'conditionQBEnabled',
            'condition_qb_serialization': 'conditionQBSerialization',
            'created': 'created',
            'display_expression': 'displayExpression',
            'display_expression_qb_enabled': 'displayExpressionQBEnabled',
            'display_expression_qb_serialization': 'displayExpressionQBSerialization',
            'event': 'event',
            'failing_host_label_pairs_override': 'failingHostLabelPairsOverride',
            'hosts_used': 'hostsUsed',
            'in_maintenance_host_label_pairs': 'inMaintenanceHostLabelPairs',
            'in_trash': 'inTrash',
            'last_error_message': 'lastErrorMessage',
            'last_failed_time': 'lastFailedTime',
            'last_updated': 'lastUpdated',
            'metrics_used': 'metricsUsed',
            'minutes': 'minutes',
            'name': 'name',
            'notificants': 'notificants',
            'prefiring_host_label_pairs': 'prefiringHostLabelPairs',
            'query_failing': 'queryFailing',
            'resolve_after_minutes': 'resolveAfterMinutes',
            'severity': 'severity',
            'snoozed': 'snoozed',
            'tags': 'tags',
            'target': 'target',
            'update_user_id': 'updateUserId',
            'updated': 'updated'
        }

        self._active_maintenance_windows = None
        self._additional_information = None
        self._condition = None
        self._condition_qb_enabled = False
        self._condition_qb_serialization = None
        self._created = None
        self._display_expression = None
        self._display_expression_qb_enabled = False
        self._display_expression_qb_serialization = None
        self._event = None
        self._failing_host_label_pairs_override = None
        self._hosts_used = None
        self._in_maintenance_host_label_pairs = None
        self._in_trash = False
        self._last_error_message = None
        self._last_failed_time = None
        self._last_updated = None
        self._metrics_used = None
        self._minutes = None
        self._name = None
        self._notificants = None
        self._prefiring_host_label_pairs = None
        self._query_failing = False
        self._resolve_after_minutes = None
        self._severity = None
        self._snoozed = None
        self._tags = None
        self._target = None
        self._update_user_id = None
        self._updated = None

    @property
    def active_maintenance_windows(self):
        """
        Gets the active_maintenance_windows of this Alert.


        :return: The active_maintenance_windows of this Alert.
        :rtype: list[str]
        """
        return self._active_maintenance_windows

    @active_maintenance_windows.setter
    def active_maintenance_windows(self, active_maintenance_windows):
        """
        Sets the active_maintenance_windows of this Alert.


        :param active_maintenance_windows: The active_maintenance_windows of this Alert.
        :type: list[str]
        """
        self._active_maintenance_windows = active_maintenance_windows

    @property
    def additional_information(self):
        """
        Gets the additional_information of this Alert.
        Additional information of the alert for runbooks, etc.

        :return: The additional_information of this Alert.
        :rtype: str
        """
        return self._additional_information

    @additional_information.setter
    def additional_information(self, additional_information):
        """
        Sets the additional_information of this Alert.
        Additional information of the alert for runbooks, etc.

        :param additional_information: The additional_information of this Alert.
        :type: str
        """
        self._additional_information = additional_information

    @property
    def condition(self):
        """
        Gets the condition of this Alert.
        The condition in which to evaluate whether the alert is firing

        :return: The condition of this Alert.
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """
        Sets the condition of this Alert.
        The condition in which to evaluate whether the alert is firing

        :param condition: The condition of this Alert.
        :type: str
        """
        self._condition = condition

    @property
    def condition_qb_enabled(self):
        """
        Gets the condition_qb_enabled of this Alert.


        :return: The condition_qb_enabled of this Alert.
        :rtype: bool
        """
        return self._condition_qb_enabled

    @condition_qb_enabled.setter
    def condition_qb_enabled(self, condition_qb_enabled):
        """
        Sets the condition_qb_enabled of this Alert.


        :param condition_qb_enabled: The condition_qb_enabled of this Alert.
        :type: bool
        """
        self._condition_qb_enabled = condition_qb_enabled

    @property
    def condition_qb_serialization(self):
        """
        Gets the condition_qb_serialization of this Alert.


        :return: The condition_qb_serialization of this Alert.
        :rtype: str
        """
        return self._condition_qb_serialization

    @condition_qb_serialization.setter
    def condition_qb_serialization(self, condition_qb_serialization):
        """
        Sets the condition_qb_serialization of this Alert.


        :param condition_qb_serialization: The condition_qb_serialization of this Alert.
        :type: str
        """
        self._condition_qb_serialization = condition_qb_serialization

    @property
    def created(self):
        """
        Gets the created of this Alert.
        The creation time in milliseconds for the alert

        :return: The created of this Alert.
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this Alert.
        The creation time in milliseconds for the alert

        :param created: The created of this Alert.
        :type: int
        """
        self._created = created

    @property
    def display_expression(self):
        """
        Gets the display_expression of this Alert.


        :return: The display_expression of this Alert.
        :rtype: str
        """
        return self._display_expression

    @display_expression.setter
    def display_expression(self, display_expression):
        """
        Sets the display_expression of this Alert.


        :param display_expression: The display_expression of this Alert.
        :type: str
        """
        self._display_expression = display_expression

    @property
    def display_expression_qb_enabled(self):
        """
        Gets the display_expression_qb_enabled of this Alert.


        :return: The display_expression_qb_enabled of this Alert.
        :rtype: bool
        """
        return self._display_expression_qb_enabled

    @display_expression_qb_enabled.setter
    def display_expression_qb_enabled(self, display_expression_qb_enabled):
        """
        Sets the display_expression_qb_enabled of this Alert.


        :param display_expression_qb_enabled: The display_expression_qb_enabled of this Alert.
        :type: bool
        """
        self._display_expression_qb_enabled = display_expression_qb_enabled

    @property
    def display_expression_qb_serialization(self):
        """
        Gets the display_expression_qb_serialization of this Alert.


        :return: The display_expression_qb_serialization of this Alert.
        :rtype: str
        """
        return self._display_expression_qb_serialization

    @display_expression_qb_serialization.setter
    def display_expression_qb_serialization(self, display_expression_qb_serialization):
        """
        Sets the display_expression_qb_serialization of this Alert.


        :param display_expression_qb_serialization: The display_expression_qb_serialization of this Alert.
        :type: str
        """
        self._display_expression_qb_serialization = display_expression_qb_serialization

    @property
    def event(self):
        """
        Gets the event of this Alert.
        The event associated with the firing of the alert. Can be null if the alert has never fired. If the alert is not currently firing, the event holds the last known firing of the alert

        :return: The event of this Alert.
        :rtype: ReportEvent
        """
        return self._event

    @event.setter
    def event(self, event):
        """
        Sets the event of this Alert.
        The event associated with the firing of the alert. Can be null if the alert has never fired. If the alert is not currently firing, the event holds the last known firing of the alert

        :param event: The event of this Alert.
        :type: ReportEvent
        """
        self._event = event

    @property
    def failing_host_label_pairs_override(self):
        """
        Gets the failing_host_label_pairs_override of this Alert.
        Failing host/metric pairs X

        :return: The failing_host_label_pairs_override of this Alert.
        :rtype: list[HostLabelPair]
        """
        return self._failing_host_label_pairs_override

    @failing_host_label_pairs_override.setter
    def failing_host_label_pairs_override(self, failing_host_label_pairs_override):
        """
        Sets the failing_host_label_pairs_override of this Alert.
        Failing host/metric pairs X

        :param failing_host_label_pairs_override: The failing_host_label_pairs_override of this Alert.
        :type: list[HostLabelPair]
        """
        self._failing_host_label_pairs_override = failing_host_label_pairs_override

    @property
    def hosts_used(self):
        """
        Gets the hosts_used of this Alert.


        :return: The hosts_used of this Alert.
        :rtype: list[str]
        """
        return self._hosts_used

    @hosts_used.setter
    def hosts_used(self, hosts_used):
        """
        Sets the hosts_used of this Alert.


        :param hosts_used: The hosts_used of this Alert.
        :type: list[str]
        """
        self._hosts_used = hosts_used

    @property
    def in_maintenance_host_label_pairs(self):
        """
        Gets the in_maintenance_host_label_pairs of this Alert.


        :return: The in_maintenance_host_label_pairs of this Alert.
        :rtype: list[HostLabelPair]
        """
        return self._in_maintenance_host_label_pairs

    @in_maintenance_host_label_pairs.setter
    def in_maintenance_host_label_pairs(self, in_maintenance_host_label_pairs):
        """
        Sets the in_maintenance_host_label_pairs of this Alert.


        :param in_maintenance_host_label_pairs: The in_maintenance_host_label_pairs of this Alert.
        :type: list[HostLabelPair]
        """
        self._in_maintenance_host_label_pairs = in_maintenance_host_label_pairs

    @property
    def in_trash(self):
        """
        Gets the in_trash of this Alert.


        :return: The in_trash of this Alert.
        :rtype: bool
        """
        return self._in_trash

    @in_trash.setter
    def in_trash(self, in_trash):
        """
        Sets the in_trash of this Alert.


        :param in_trash: The in_trash of this Alert.
        :type: bool
        """
        self._in_trash = in_trash

    @property
    def last_error_message(self):
        """
        Gets the last_error_message of this Alert.


        :return: The last_error_message of this Alert.
        :rtype: str
        """
        return self._last_error_message

    @last_error_message.setter
    def last_error_message(self, last_error_message):
        """
        Sets the last_error_message of this Alert.


        :param last_error_message: The last_error_message of this Alert.
        :type: str
        """
        self._last_error_message = last_error_message

    @property
    def last_failed_time(self):
        """
        Gets the last_failed_time of this Alert.


        :return: The last_failed_time of this Alert.
        :rtype: int
        """
        return self._last_failed_time

    @last_failed_time.setter
    def last_failed_time(self, last_failed_time):
        """
        Sets the last_failed_time of this Alert.


        :param last_failed_time: The last_failed_time of this Alert.
        :type: int
        """
        self._last_failed_time = last_failed_time

    @property
    def last_updated(self):
        """
        Gets the last_updated of this Alert.


        :return: The last_updated of this Alert.
        :rtype: int
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """
        Sets the last_updated of this Alert.


        :param last_updated: The last_updated of this Alert.
        :type: int
        """
        self._last_updated = last_updated

    @property
    def metrics_used(self):
        """
        Gets the metrics_used of this Alert.


        :return: The metrics_used of this Alert.
        :rtype: list[str]
        """
        return self._metrics_used

    @metrics_used.setter
    def metrics_used(self, metrics_used):
        """
        Sets the metrics_used of this Alert.


        :param metrics_used: The metrics_used of this Alert.
        :type: list[str]
        """
        self._metrics_used = metrics_used

    @property
    def minutes(self):
        """
        Gets the minutes of this Alert.
        The time to elapse before firing or resolving the alert when the condition evaluates to true or false (respectively)

        :return: The minutes of this Alert.
        :rtype: int
        """
        return self._minutes

    @minutes.setter
    def minutes(self, minutes):
        """
        Sets the minutes of this Alert.
        The time to elapse before firing or resolving the alert when the condition evaluates to true or false (respectively)

        :param minutes: The minutes of this Alert.
        :type: int
        """
        self._minutes = minutes

    @property
    def name(self):
        """
        Gets the name of this Alert.
        The name of the alert

        :return: The name of this Alert.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Alert.
        The name of the alert

        :param name: The name of this Alert.
        :type: str
        """
        self._name = name

    @property
    def notificants(self):
        """
        Gets the notificants of this Alert.


        :return: The notificants of this Alert.
        :rtype: list[str]
        """
        return self._notificants

    @notificants.setter
    def notificants(self, notificants):
        """
        Sets the notificants of this Alert.


        :param notificants: The notificants of this Alert.
        :type: list[str]
        """
        self._notificants = notificants

    @property
    def prefiring_host_label_pairs(self):
        """
        Gets the prefiring_host_label_pairs of this Alert.


        :return: The prefiring_host_label_pairs of this Alert.
        :rtype: list[HostLabelPair]
        """
        return self._prefiring_host_label_pairs

    @prefiring_host_label_pairs.setter
    def prefiring_host_label_pairs(self, prefiring_host_label_pairs):
        """
        Sets the prefiring_host_label_pairs of this Alert.


        :param prefiring_host_label_pairs: The prefiring_host_label_pairs of this Alert.
        :type: list[HostLabelPair]
        """
        self._prefiring_host_label_pairs = prefiring_host_label_pairs

    @property
    def query_failing(self):
        """
        Gets the query_failing of this Alert.


        :return: The query_failing of this Alert.
        :rtype: bool
        """
        return self._query_failing

    @query_failing.setter
    def query_failing(self, query_failing):
        """
        Sets the query_failing of this Alert.


        :param query_failing: The query_failing of this Alert.
        :type: bool
        """
        self._query_failing = query_failing

    @property
    def resolve_after_minutes(self):
        """
        Gets the resolve_after_minutes of this Alert.


        :return: The resolve_after_minutes of this Alert.
        :rtype: int
        """
        return self._resolve_after_minutes

    @resolve_after_minutes.setter
    def resolve_after_minutes(self, resolve_after_minutes):
        """
        Sets the resolve_after_minutes of this Alert.


        :param resolve_after_minutes: The resolve_after_minutes of this Alert.
        :type: int
        """
        self._resolve_after_minutes = resolve_after_minutes

    @property
    def severity(self):
        """
        Gets the severity of this Alert.
        The severity of the alert

        :return: The severity of this Alert.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """
        Sets the severity of this Alert.
        The severity of the alert

        :param severity: The severity of this Alert.
        :type: str
        """
        allowed_values = ["INFO", "SMOKE", "WARN", "SEVERE"]
        if severity not in allowed_values:
            raise ValueError(
                "Invalid value for `severity`, must be one of {0}"
                .format(allowed_values)
            )
        self._severity = severity

    @property
    def snoozed(self):
        """
        Gets the snoozed of this Alert.
        Milliseconds since the epoch the alert is snoozed until. A value in the past indicates that the alert is not snoozed

        :return: The snoozed of this Alert.
        :rtype: int
        """
        return self._snoozed

    @snoozed.setter
    def snoozed(self, snoozed):
        """
        Sets the snoozed of this Alert.
        Milliseconds since the epoch the alert is snoozed until. A value in the past indicates that the alert is not snoozed

        :param snoozed: The snoozed of this Alert.
        :type: int
        """
        self._snoozed = snoozed

    @property
    def tags(self):
        """
        Gets the tags of this Alert.
        Associated tags

        :return: The tags of this Alert.
        :rtype: Tags
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this Alert.
        Associated tags

        :param tags: The tags of this Alert.
        :type: Tags
        """
        self._tags = tags

    @property
    def target(self):
        """
        Gets the target of this Alert.
        The email address or integration endpoint (such as PagerDuty) to notify when the alert state changes

        :return: The target of this Alert.
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """
        Sets the target of this Alert.
        The email address or integration endpoint (such as PagerDuty) to notify when the alert state changes

        :param target: The target of this Alert.
        :type: str
        """
        self._target = target

    @property
    def update_user_id(self):
        """
        Gets the update_user_id of this Alert.


        :return: The update_user_id of this Alert.
        :rtype: str
        """
        return self._update_user_id

    @update_user_id.setter
    def update_user_id(self, update_user_id):
        """
        Sets the update_user_id of this Alert.


        :param update_user_id: The update_user_id of this Alert.
        :type: str
        """
        self._update_user_id = update_user_id

    @property
    def updated(self):
        """
        Gets the updated of this Alert.
        The last known update time of the alert by a user

        :return: The updated of this Alert.
        :rtype: int
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """
        Sets the updated of this Alert.
        The last known update time of the alert by a user

        :param updated: The updated of this Alert.
        :type: int
        """
        self._updated = updated

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

