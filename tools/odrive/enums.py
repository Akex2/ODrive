
# TODO: This is dangerous. Transmit as part of the JSON

AXIS_STATE_UNDEFINED = 0
AXIS_STATE_IDLE = 1
AXIS_STATE_STARTUP_SEQUENCE = 2
AXIS_STATE_FULL_CALIBRATION_SEQUENCE = 3
AXIS_STATE_MOTOR_CALIBRATION = 4
AXIS_STATE_SENSORLESS_CONTROL = 5
AXIS_STATE_ENCODER_INDEX_SEARCH = 6
AXIS_STATE_ENCODER_OFFSET_CALIBRATION = 7
AXIS_STATE_CLOSED_LOOP_CONTROL = 8

AXIS_ERROR_NONE = 0
AXIS_ERROR_INVALID_STATE = 1
#AXIS_ERROR_DC_BUS_UNDER_VOLTAGE = 2
#AXIS_ERROR_DC_BUS_OVER_VOLTAGE = 3
#AXIS_ERROR_CURRENT_MEASUREMENT_TIMEOUT = 4
#AXIS_ERROR_CONTROL_LOOP_TIMEOUT = 5
#AXIS_ERROR_MOTOR_FAILED = 6
#AXIS_ERROR_SENSORLESS_ESTIMATOR_FAILED = 7
#AXIS_ERROR_ENCODER_FAILED = 8
#AXIS_ERROR_CONTROLLER_FAILED = 9
#AXIS_ERROR_POS_CTRL_DURING_SENSORLESS = 10

MOTOR_TYPE_HIGH_CURRENT = 0
#MOTOR_TYPE_LOW_CURRENT = 1
MOTOR_TYPE_GIMBAL = 2

CTRL_MODE_VOLTAGE_CONTROL = 0
CTRL_MODE_CURRENT_CONTROL = 1
CTRL_MODE_VELOCITY_CONTROL = 2
CTRL_MODE_POSITION_CONTROL = 3
