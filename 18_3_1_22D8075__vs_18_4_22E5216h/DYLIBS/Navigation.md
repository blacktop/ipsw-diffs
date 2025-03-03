## Navigation

> `/System/Library/PrivateFrameworks/Navigation.framework/Navigation`

```diff

-2340.33.11.14.1
-  __TEXT.__text: 0x104728
-  __TEXT.__auth_stubs: 0x1870
-  __TEXT.__objc_methlist: 0xee80
-  __TEXT.__const: 0x924
-  __TEXT.__cstring: 0x1827e
-  __TEXT.__oslogstring: 0xd140
-  __TEXT.__swift5_typeref: 0x225
-  __TEXT.__constg_swiftt: 0x43c
-  __TEXT.__swift5_reflstr: 0x178
-  __TEXT.__swift5_fieldmd: 0x1ac
+2340.34.9.12.11
+  __TEXT.__text: 0x10513c
+  __TEXT.__auth_stubs: 0x18c0
+  __TEXT.__objc_methlist: 0x1127c
+  __TEXT.__const: 0x9f4
+  __TEXT.__dlopen_cstrs: 0xb4
+  __TEXT.__cstring: 0x18197
+  __TEXT.__swift5_typeref: 0x2b9
+  __TEXT.__constg_swiftt: 0x494
+  __TEXT.__swift5_fieldmd: 0x1f0
+  __TEXT.__swift5_reflstr: 0x1a8
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_proto: 0x10
-  __TEXT.__swift5_types: 0x34
+  __TEXT.__swift5_capture: 0x20
+  __TEXT.__swift5_proto: 0x14
+  __TEXT.__swift5_types: 0x3c
+  __TEXT.__swift_as_entry: 0x8
+  __TEXT.__swift_as_ret: 0x8
+  __TEXT.__oslogstring: 0xd17e
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__gcc_except_tab: 0x4f38
+  __TEXT.__gcc_except_tab: 0x4f40
   __TEXT.__ustring: 0x222
-  __TEXT.__dlopen_cstrs: 0xb4
-  __TEXT.__unwind_info: 0x3f98
-  __TEXT.__eh_frame: 0x180
+  __TEXT.__unwind_info: 0x3f18
+  __TEXT.__eh_frame: 0x250
   __TEXT.__objc_classname: 0x23c7
-  __TEXT.__objc_methname: 0x2686f
-  __TEXT.__objc_methtype: 0x7c03
-  __TEXT.__objc_stubs: 0x1d900
-  __DATA_CONST.__got: 0xcc0
-  __DATA_CONST.__const: 0x62a0
+  __TEXT.__objc_methname: 0x267e2
+  __TEXT.__objc_methtype: 0x7bf2
+  __TEXT.__objc_stubs: 0x1d8c0
+  __DATA_CONST.__got: 0xce0
+  __DATA_CONST.__const: 0x62c0
   __DATA_CONST.__objc_classlist: 0x778
   __DATA_CONST.__objc_catlist: 0x138
   __DATA_CONST.__objc_protolist: 0x298
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8468
+  __DATA_CONST.__objc_selrefs: 0x85e0
   __DATA_CONST.__objc_protorefs: 0xe8
   __DATA_CONST.__objc_superrefs: 0x4e0
-  __DATA_CONST.__objc_arraydata: 0x1c0
-  __AUTH_CONST.__auth_got: 0xc50
-  __AUTH_CONST.__auth_ptr: 0x98
-  __AUTH_CONST.__const: 0x2760
-  __AUTH_CONST.__cfstring: 0xd140
-  __AUTH_CONST.__objc_const: 0x20718
+  __DATA_CONST.__objc_arraydata: 0x1e8
+  __AUTH_CONST.__auth_got: 0xc78
+  __AUTH_CONST.__auth_ptr: 0xb0
+  __AUTH_CONST.__const: 0x28b0
+  __AUTH_CONST.__cfstring: 0xd240
+  __AUTH_CONST.__objc_const: 0x1c320
   __AUTH_CONST.__objc_intobj: 0x900
-  __AUTH_CONST.__objc_arrayobj: 0x168
+  __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_doubleobj: 0xe0
-  __AUTH.__objc_data: 0x6f8
+  __AUTH.__objc_data: 0x700
   __AUTH.__data: 0x198
-  __DATA.__objc_ivar: 0x12a0
-  __DATA.__data: 0x28a8
-  __DATA.__bss: 0x248
+  __DATA.__objc_ivar: 0x1290
+  __DATA.__data: 0x28e8
+  __DATA.__bss: 0x2c8
   __DATA.__common: 0x110
   __DATA_DIRTY.__objc_ivar: 0x1b4
   __DATA_DIRTY.__objc_data: 0x4710

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_errno.dylib
   - /usr/lib/swift/libswift_math.dylib
   - /usr/lib/swift/libswift_signal.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 6138
-  Symbols:   6977
-  CStrings:  10588
+  Functions: 6130
+  Symbols:   6991
+  CStrings:  10584
 
Symbols:
+ __Block_copy
+ __Block_release
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initWithCopy
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_deallocObject
+ _swift_task_alloc
+ _swift_task_dealloc
+ _swift_task_switch
- _NSFileCreationDate
CStrings:
+ "\x02\x12\x1f\t!"
+ "\nCREATE TABLE info\n(\n    -- 0: Navigation\n    -- 1: Route Planning\n    -- 2: Custom Route Creation\n    trace_type              INTEGER NOT NULL,\n    \n    name                    TEXT,               -- Deprecated and unset\n    version                 INTEGER NOT NULL,\n    recording_start_time    NUMERIC,            -- All relative timestamps in other tables are relative to this time.\n    directions_start_time   NUMERIC,            -- The time of the first directions request. This is approximately the time when\n                                                -- the user entered route preview, but not exactly. Additionally, when multiple\n                                                -- directions requests are made in route preview (i.e. multi-stop routes) this will\n                                                -- be the time of the last request.\n    navigation_start_time   NUMERIC,            -- This is typically the same as `recording_start_time` (though not guaranteed in future versions)\n    navigation_end_time     NUMERIC,\n    start_time              INTEGER,            -- Deprecated and unset, use start_directions_time or start_navigation_time instead\n    end_time                INTEGER,            -- Deprecated and unset, use end_navigation_time instead\n    start_data              BLOB,               -- Deprecated and unset, use waypoints_data in directions table instead\n    end_data                BLOB,               -- Deprecated and unset, use waypoints_data in directions table instead\n    simulation              INTEGER,\n    route_genius            INTEGER,            -- Deprecated and unset, we don't record navtraces for Route Genius\n    cl_mapmatch             INTEGER,            -- Deprecated and unset, as of Azul this will always be true\n    original_version        INTEGER,\n    initial_course          NUMERIC,            -- Deprecated and unset, use course in locations table instead\n    directions_url          TEXT\n);\n\nCREATE TABLE environment_info\n(\n    name    TEXT NOT NULL,\n    value   TEXT NOT NULL\n);\n\nCREATE TABLE debug_settings\n(\n    setting_name    TEXT,\n    setting_value   TEXT\n);\n\nCREATE TABLE audio_settings\n(\n    db_timestamp        NUMERIC NOT NULL,\n    pause_spoken_audio  INTEGER,\n    volume_setting      INTEGER\n);\n\nCREATE TABLE misc_info\n(\n    key     TEXT NOT NULL,\n    value   NOT NULL        -- Type intentionally unspecified. This column can support multiple types.\n);\n\nCREATE TABLE bookmarks\n(\n    id                  INTEGER PRIMARY KEY ASC AUTOINCREMENT,\n    timestamp           NUMERIC NOT NULL,\n    screenshot_data     BLOB            -- PNG screenshot\n);\n\nCREATE TABLE stylesheets\n(\n    id                  INTEGER PRIMARY KEY ASC AUTOINCREMENT,\n    stylesheet_name     TEXT,\n    stylesheet_data     BLOB\n);\n        \nCREATE TABLE locations\n(\n    id                      INTEGER PRIMARY KEY ASC AUTOINCREMENT,\n    db_timestamp            NUMERIC NOT NULL,\n    cl_timestamp            NUMERIC,\n    latitude                NUMERIC,\n    longitude               NUMERIC,\n    raw_latitude            NUMERIC,\n    raw_longitude           NUMERIC,\n    horizontal_accuracy     NUMERIC,\n    vertical_accuracy       NUMERIC,\n    altitude                NUMERIC,\n    speed                   NUMERIC,\n    speed_accuracy          NUMERIC,\n    course                  NUMERIC,\n    raw_course              NUMERIC,\n    course_accuracy         NUMERIC,\n    type                    INTEGER,    -- CLLocationType in CLLocationType_Private.h\n    reference_frame         INTEGER,    -- CLClientLocationReferenceFrame in CLClientTypes.h\n    raw_reference_frame     INTEGER,    -- CLClientLocationReferenceFrame in CLClientTypes.h\n    error_data              BLOB,       -- PB Serialized NSError\n    event_type              INTEGER,\n    corrected_latitude      NUMERIC,\n    corrected_longitude     NUMERIC,\n    corrected_course        NUMERIC,\n    match_type              NUMERIC,\n    active_transport_type   INTEGER DEFAULT 4, -- default is the unknown transport type\n    match_info_quality      INTEGER,\n    match_info_latitude     NUMERIC,\n    match_info_longitude    NUMERIC,\n    match_info_course       NUMERIC,\n    match_info_form_of_way  INTEGER,\n    match_info_road_class   INTEGER,\n    match_info_shifted      INTEGER,\n    speed_limit             INTEGER,\n    shield_text             TEXT,\n    shield_type             INTEGER\n);\n\nCREATE TABLE location_match_info\n(\n    location_id                     INTEGER REFERENCES locations(id),\n    route_coordinate                NUMERIC,\n    step_index                      INTEGER,\n    form_of_way                     INTEGER,\n    route_match_score               NUMERIC,\n    distance_from_route             NUMERIC,\n    max_route_distance              NUMERIC,\n    route_distance_match_score      NUMERIC,\n    route_distance_weight           NUMERIC,\n    route_course_delta              NUMERIC,\n    max_route_course_delta          NUMERIC,\n    route_course_match_score        NUMERIC,\n    route_course_weight             NUMERIC,\n    road_width_on_route             NUMERIC,\n    distance_from_road              NUMERIC,\n    road_course_delta               NUMERIC,\n    distance_from_nearest_junction  NUMERIC\n);\n\nCREATE TABLE directions\n(\n    id                      INTEGER PRIMARY KEY ASC AUTOINCREMENT,\n    request_timestamp       NUMERIC,\n    response_timestamp      NUMERIC,\n    request_data            BLOB,               -- PB Serialized GEODirectionsRequest\n    response_data           BLOB,               -- PB Serialized GEODirectionsResponse\n    response_error_data     BLOB,               -- PB Serialized NSError\n    waypoints_data          BLOB,               -- NSArray of GEOComposedWaypoint\n    selected_route_index    INTEGER DEFAULT 0\n);\n\nCREATE TABLE eta_traffic_updates\n(\n    id                      INTEGER PRIMARY KEY ASC AUTOINCREMENT,\n    request_timestamp       NUMERIC NOT NULL,\n    response_timestamp      NUMERIC,\n    request_data            BLOB NOT NULL,  -- PB Serialized\n    response_data           BLOB,           -- PB Serialized\n    response_error_data     BLOB,           -- PB Serialized NSError\n    destination_name        TEXT,\n    dodgeball_alert_type    NUMERIC         -- 0 = Blockage, 1 = Incident, 2 = Reroute, blank = None\n);\n\nCREATE TABLE realtime_transit_updates\n(\n    id                      INTEGER PRIMARY KEY ASC AUTOINCREMENT,\n    timestamp               NUMERIC NOT NULL,\n    request_data            BLOB,           -- PB Serialized\n    response_data           BLOB,           -- PB Serialized\n    response_error_data     BLOB            -- PB Serialized NSError\n);\n\nCREATE TABLE vehicle_speed_data\n(\n    relative_timestamp  NUMERIC NOT NULL,\n    absolute_timestamp  NUMERIC NOT NULL,\n    speed               NUMERIC NOT NULL\n);\n\nCREATE TABLE vehicle_heading_data\n(\n    relative_timestamp  NUMERIC NOT NULL,\n    absolute_timestamp  NUMERIC NOT NULL,\n    heading             NUMERIC NOT NULL\n);\n\nCREATE TABLE motion_data\n(\n    relative_timestamp  NUMERIC NOT NULL,\n    absolute_timestamp  NUMERIC NOT NULL,\n    type                INTEGER,\n    exit_type           INTEGER,\n    confidence          INTEGER\n);\n\nCREATE TABLE compass_heading_data\n(\n    relative_timestamp  NUMERIC NOT NULL,\n    absolute_timestamp  NUMERIC NOT NULL,\n    true_heading        NUMERIC,\n    magnetic_heading    NUMERIC,\n    accuracy            NUMERIC\n);\n\nCREATE TABLE ev_data\n(\n    relative_timestamp              NUMERIC NOT NULL,\n    absolute_timestamp              NUMERIC NOT NULL,\n    identifier                      TEXT,\n    current_range_m                 NUMERIC,\n    max_range_m                     NUMERIC,\n    battery_percentage              NUMERIC,\n    min_battery_capacity_kwh        NUMERIC,\n    current_battery_capacity_kwh    NUMERIC,\n    max_battery_capacity_kwh        NUMERIC,\n    consumption_arguments           TEXT,\n    charging_arguments              TEXT,\n    is_charging                     NUMERIC,\n    active_connector                NUMERIC,\n    vehicle_state_origin            NUMERIC,\n    vehicle_data                    BLOB -- Serialized VGVehicle\n);\n\nCREATE TABLE navigation_events\n(\n    relative_timestamp      NUMERIC NOT NULL,\n    absolute_timestamp      NUMERIC NOT NULL,\n    last_location_id        INTEGER, -- Will be removed soon - TODO: rdar://139912166 (Remove last_location_id from the navigation_events table in the navtrace schema)\n    event_id                INTEGER DEFAULT 0 REFERENCES navigation_event_types(event_id),\n    event_description       TEXT\n\n    -- Hint: Use the following query to see event types as strings instead of numbers:\n    --       SELECT * FROM navigation_events_view;\n);\n\nCREATE TABLE navigation_event_types\n(\n    event_id        INTEGER NOT NULL PRIMARY KEY,\n    event_name      TEXT NOT NULL\n);\n\nCREATE TABLE annotated_user_behavior\n(\n    timestamp   NUMERIC NOT NULL,\n    event       INTEGER NOT NULL /* event corresponds to the MNTraceUserBehaviorEvent enum in MNTrace.h. Event types:\n        Unknown = 0\n        Reroute = 1\n        OffRoute = 2\n    */\n);\n\nCREATE TABLE annotated_user_environments\n(\n    start_timestamp     NUMERIC NOT NULL,\n    end_timestamp       NUMERIC NOT NULL,\n    environment_type    INTEGER NOT NULL /* environment_type corresponds to the MNTraceUserEnvironmentType enum in MNTrace.h. Environment types:\n        Unknown = 0\n        UrbanCanyon = 1\n        DeepUrbanCanyon = 2\n        TallTrees = 3\n        Tunnel = 4\n        Overpass = 5\n        Frontage = 6\n        Freeway = 7\n    */\n);\n\nCREATE TABLE navigation_updates\n(\n    timestamp                   NUMERIC,\n    type                        NUMERIC,\n    parameters                  BLOB                  -- NSDictionary specific to parameters based on type of event\n);\n\n-- Custom Route Creation\n\nCREATE TABLE custom_route_creation_actions (\n    request_timestamp       NUMERIC,\n    response_timestamp      NUMERIC,\n    request_data            BLOB,   -- GEODirectionsRequest\n    response_data           BLOB,   -- GEODirectionsResponse\n    response_error_data     BLOB,   -- NSError\n    anchor_points_data      BLOB,   -- NSArray of GEOComposedRouteAnchorPoint\n    action                  INTEGER -- MNRouteEditorAction in MNNavigationEnums.h\n);\n\n-- Views\n\n-- info\n\nCREATE VIEW info_view AS\n    SELECT\n        version,\n        original_version,\n        strftime('%H:%M:%S', time(recording_start_time, 'unixepoch', 'localtime')) AS recording_start_time,\n        strftime('%H:%M:%S', time(directions_start_time, 'unixepoch', 'localtime')) AS directions_start_time,\n        strftime('%H:%M:%S', time(navigation_start_time, 'unixepoch', 'localtime')) AS navigation_start_time,\n        strftime('%H:%M:%S', time(navigation_end_time, 'unixepoch', 'localtime')) AS navigation_end_time,\n        simulation\n    FROM\n        info;\n\n-- directions\n\nCREATE VIEW directions_view AS\n    SELECT\n        id,\n        PRINTF(\"%.3f\", request_timestamp) AS request_time,\n        PRINTF(\"%.3f\", response_timestamp) AS response_time,\n        LENGTH(request_data) AS request,\n        LENGTH(response_data) AS response,\n        LENGTH(response_error_data) AS error,\n        LENGTH(waypoints_data) AS waypoints,\n        selected_route_index\n    FROM\n        directions;\n         \n-- eta_traffic_updates\n\nCREATE VIEW etau_view AS\n    SELECT\n        id,\n        PRINTF(\"%.3f\", request_timestamp) AS request_time,\n        PRINTF(\"%.3f\", response_timestamp) AS response_time,\n        LENGTH(request_data) AS request,\n        LENGTH(response_data) AS response,\n        LENGTH(response_error_data) AS error,\n        destination_name AS destination\n    FROM\n        eta_traffic_updates;\n\n-- navigation_events\n\nCREATE VIEW navigation_events_view AS\n    SELECT\n        PRINTF(\"%.3f\", relative_timestamp) AS relative_time,\n        PRINTF(\"%d\", absolute_timestamp) AS absolute_time,\n        strftime('%H:%M:%S', time(absolute_timestamp, 'unixepoch', 'localtime')) AS time,\n        last_location_id AS location,\n        event_name,\n        event_description\n    FROM\n        navigation_events INNER JOIN navigation_event_types ON navigation_events.event_id = navigation_event_types.event_id;\n\n-- ev_data\n\nCREATE VIEW ev_data_view as\n    SELECT\n        PRINTF(\"%.1f\", relative_timestamp) AS time,\n        strftime('%H:%M:%S', time(absolute_timestamp, 'unixepoch', 'localtime')) AS date,\n        PRINTF(\"%.0f%%\", battery_percentage * 100) AS \"battery%\",\n        PRINTF(\"%.1f\", current_range_m) AS \"range (meters)\",\n        PRINTF(\"%.1f\", current_battery_capacity_kwh) AS \"capacity (kwh)\",\n        is_charging,\n        CASE WHEN length(vehicle_data) > 0 THEN identifier END as identifier\n    FROM\n        ev_data;\n\n-- custom_route_creation_actions\n\nCREATE VIEW route_creation_actions_view AS\n    SELECT\n        rowid AS 'Index',\n        PRINTF(\"%.3f\", request_timestamp) AS 'Request Time',\n        PRINTF(\"%.3f\", response_timestamp) AS 'Response Time',\n        LENGTH(request_data) AS 'Request',\n        LENGTH(response_data) AS 'Response',\n        LENGTH(response_error_data) AS 'Error',\n        LENGTH(anchor_points_data) AS 'Anchor Points',\n        CASE action\n            WHEN 0 THEN 'Unset'\n            WHEN 1 THEN 'Append Anchor'\n            WHEN 2 THEN 'Delete Anchor'\n            WHEN 101 THEN 'Reverse'\n            WHEN 102 THEN 'Out and Back'\n            WHEN 103 THEN 'Close Loop'\n            WHEN 1001 THEN 'Undo'\n            WHEN 1002 THEN 'Redo'\n            ELSE 'Unknown'\n        END AS 'Action'\n    FROM\n        custom_route_creation_actions;\n"
+ "\x11\x13"
+ "\x15\x12"
+ "\"%@\" has no modification date. Ignoring."
+ "%0.2fs"
+ "/System/AppleInternal/Library/Frameworks/ConditionInducer.framework/ConditionInducer"
+ "/System/AppleInternal/Library/Frameworks/CoreAutomationDevice.framework/CoreAutomationDevice"
+ "/System/AppleInternal/Library/Frameworks/CoreRoutine.framework/CoreRoutine"
+ "/System/AppleInternal/Library/Frameworks/CoreWiFi.framework/CoreWiFi"
+ ":absolute_timestamp"
+ ":event_description"
+ ":event_id"
+ ":relative_timestamp"
+ "Assertion failed: _route != ((void*)0)"
+ "Assertion failed: finishedHandler != ((void*)0)"
+ "INSERT INTO navigation_events (relative_timestamp, absolute_timestamp, event_id, event_description) VALUES (:relative_timestamp, :absolute_timestamp, :event_id, :event_description)"
+ "Removed trace \"%@\" because its last modified date is too old: %@"
+ "T@\"GEOComposedGuidanceEvent\",N,R,V_guidanceEvent"
+ "_joinClauses"
+ "absolute_timestamp"
+ "event_description"
+ "event_id"
+ "event_name"
+ "innerJoin:where:equals:"
+ "navigation_event_types"
+ "navigation_events"
+ "navigation_events.event_id"
+ "recordNavigationEvent:description:"
+ "relative_timestamp"
+ "routes(for:transportType:maxRouteCount:routeAttributes:traits:)"
+ "setSource:"
+ "setSupportsArMode:"
+ "waypoint(for:requireMapItem:)"
- "\x02\x12\x1f\n\""
- "\nCREATE TABLE info\n(\n    -- 0: Navigation\n    -- 1: Route Planning\n    -- 2: Custom Route Creation\n    trace_type              INTEGER NOT NULL,\n    \n    name                    TEXT,               -- Deprecated and unset\n    version                 INTEGER NOT NULL,\n    recording_start_time    NUMERIC,            -- All relative timestamps in other tables are relative to this time.\n    directions_start_time   NUMERIC,            -- The time of the first directions request. This is approximately the time when\n                                                -- the user entered route preview, but not exactly. Additionally, when multiple\n                                                -- directions requests are made in route preview (i.e. multi-stop routes) this will\n                                                -- be the time of the last request.\n    navigation_start_time   NUMERIC,            -- This is typically the same as `recording_start_time` (though not guaranteed in future versions)\n    navigation_end_time     NUMERIC,\n    start_time              INTEGER,            -- Deprecated and unset, use start_directions_time or start_navigation_time instead\n    end_time                INTEGER,            -- Deprecated and unset, use end_navigation_time instead\n    start_data              BLOB,               -- Deprecated and unset, use waypoints_data in directions table instead\n    end_data                BLOB,               -- Deprecated and unset, use waypoints_data in directions table instead\n    simulation              INTEGER,\n    route_genius            INTEGER,            -- Deprecated and unset, we don't record navtraces for Route Genius\n    cl_mapmatch             INTEGER,            -- Deprecated and unset, as of Azul this will always be true\n    original_version        INTEGER,\n    initial_course          NUMERIC,            -- Deprecated and unset, use course in locations table instead\n    directions_url          TEXT\n);\n\nCREATE TABLE environment_info\n(\n    name    TEXT NOT NULL,\n    value   TEXT NOT NULL\n);\n\nCREATE TABLE debug_settings\n(\n    setting_name    TEXT,\n    setting_value   TEXT\n);\n\nCREATE TABLE audio_settings\n(\n    db_timestamp        NUMERIC NOT NULL,\n    pause_spoken_audio  INTEGER,\n    volume_setting      INTEGER\n);\n\nCREATE TABLE misc_info\n(\n    key     TEXT NOT NULL,\n    value   NOT NULL        -- Type intentionally unspecified. This column can support multiple types.\n);\n\nCREATE TABLE bookmarks\n(\n    id                  INTEGER PRIMARY KEY ASC AUTOINCREMENT,\n    timestamp           NUMERIC NOT NULL,\n    screenshot_data     BLOB            -- PNG screenshot\n);\n\nCREATE TABLE stylesheets\n(\n    id                  INTEGER PRIMARY KEY ASC AUTOINCREMENT,\n    stylesheet_name     TEXT,\n    stylesheet_data     BLOB\n);\n        \nCREATE TABLE locations\n(\n    id                      INTEGER PRIMARY KEY ASC AUTOINCREMENT,\n    db_timestamp            NUMERIC NOT NULL,\n    cl_timestamp            NUMERIC,\n    latitude                NUMERIC,\n    longitude               NUMERIC,\n    raw_latitude            NUMERIC,\n    raw_longitude           NUMERIC,\n    horizontal_accuracy     NUMERIC,\n    vertical_accuracy       NUMERIC,\n    altitude                NUMERIC,\n    speed                   NUMERIC,\n    speed_accuracy          NUMERIC,\n    course                  NUMERIC,\n    raw_course              NUMERIC,\n    course_accuracy         NUMERIC,\n    type                    INTEGER,    -- CLLocationType in CLLocationType_Private.h\n    reference_frame         INTEGER,    -- CLClientLocationReferenceFrame in CLClientTypes.h\n    raw_reference_frame     INTEGER,    -- CLClientLocationReferenceFrame in CLClientTypes.h\n    error_data              BLOB,       -- PB Serialized NSError\n    event_type              INTEGER,\n    corrected_latitude      NUMERIC,\n    corrected_longitude     NUMERIC,\n    corrected_course        NUMERIC,\n    match_type              NUMERIC,\n    active_transport_type   INTEGER DEFAULT 4, -- default is the unknown transport type\n    match_info_quality      INTEGER,\n    match_info_latitude     NUMERIC,\n    match_info_longitude    NUMERIC,\n    match_info_course       NUMERIC,\n    match_info_form_of_way  INTEGER,\n    match_info_road_class   INTEGER,\n    match_info_shifted      INTEGER,\n    speed_limit             INTEGER,\n    shield_text             TEXT,\n    shield_type             INTEGER\n);\n\nCREATE TABLE location_match_info\n(\n    location_id                     INTEGER REFERENCES locations(id),\n    route_coordinate                NUMERIC,\n    step_index                      INTEGER,\n    form_of_way                     INTEGER,\n    route_match_score               NUMERIC,\n    distance_from_route             NUMERIC,\n    max_route_distance              NUMERIC,\n    route_distance_match_score      NUMERIC,\n    route_distance_weight           NUMERIC,\n    route_course_delta              NUMERIC,\n    max_route_course_delta          NUMERIC,\n    route_course_match_score        NUMERIC,\n    route_course_weight             NUMERIC,\n    road_width_on_route             NUMERIC,\n    distance_from_road              NUMERIC,\n    road_course_delta               NUMERIC,\n    distance_from_nearest_junction  NUMERIC\n);\n\nCREATE TABLE directions\n(\n    id                      INTEGER PRIMARY KEY ASC AUTOINCREMENT,\n    request_timestamp       NUMERIC,\n    response_timestamp      NUMERIC,\n    request_data            BLOB,               -- PB Serialized GEODirectionsRequest\n    response_data           BLOB,               -- PB Serialized GEODirectionsResponse\n    response_error_data     BLOB,               -- PB Serialized NSError\n    waypoints_data          BLOB,               -- NSArray of GEOComposedWaypoint\n    selected_route_index    INTEGER DEFAULT 0\n);\n\nCREATE TABLE eta_traffic_updates\n(\n    id                      INTEGER PRIMARY KEY ASC AUTOINCREMENT,\n    request_timestamp       NUMERIC NOT NULL,\n    response_timestamp      NUMERIC,\n    request_data            BLOB NOT NULL,  -- PB Serialized\n    response_data           BLOB,           -- PB Serialized\n    response_error_data     BLOB,           -- PB Serialized NSError\n    destination_name        TEXT,\n    dodgeball_alert_type    NUMERIC         -- 0 = Blockage, 1 = Incident, 2 = Reroute, blank = None\n);\n\nCREATE TABLE realtime_transit_updates\n(\n    id                      INTEGER PRIMARY KEY ASC AUTOINCREMENT,\n    timestamp               NUMERIC NOT NULL,\n    request_data            BLOB,           -- PB Serialized\n    response_data           BLOB,           -- PB Serialized\n    response_error_data     BLOB            -- PB Serialized NSError\n);\n\nCREATE TABLE vehicle_speed_data\n(\n    relative_timestamp  NUMERIC NOT NULL,\n    absolute_timestamp  NUMERIC NOT NULL,\n    speed               NUMERIC NOT NULL\n);\n\nCREATE TABLE vehicle_heading_data\n(\n    relative_timestamp  NUMERIC NOT NULL,\n    absolute_timestamp  NUMERIC NOT NULL,\n    heading             NUMERIC NOT NULL\n);\n\nCREATE TABLE motion_data\n(\n    relative_timestamp  NUMERIC NOT NULL,\n    absolute_timestamp  NUMERIC NOT NULL,\n    type                INTEGER,\n    exit_type           INTEGER,\n    confidence          INTEGER\n);\n\nCREATE TABLE compass_heading_data\n(\n    relative_timestamp  NUMERIC NOT NULL,\n    absolute_timestamp  NUMERIC NOT NULL,\n    true_heading        NUMERIC,\n    magnetic_heading    NUMERIC,\n    accuracy            NUMERIC\n);\n\nCREATE TABLE ev_data\n(\n    relative_timestamp              NUMERIC NOT NULL,\n    absolute_timestamp              NUMERIC NOT NULL,\n    identifier                      TEXT,\n    current_range_m                 NUMERIC,\n    max_range_m                     NUMERIC,\n    battery_percentage              NUMERIC,\n    min_battery_capacity_kwh        NUMERIC,\n    current_battery_capacity_kwh    NUMERIC,\n    max_battery_capacity_kwh        NUMERIC,\n    consumption_arguments           TEXT,\n    charging_arguments              TEXT,\n    is_charging                     NUMERIC,\n    active_connector                NUMERIC,\n    vehicle_state_origin            NUMERIC,\n    vehicle_data                    BLOB -- Serialized VGVehicle\n);\n\nCREATE TABLE navigation_events\n(\n    relative_timestamp      NUMERIC NOT NULL,\n    absolute_timestamp      NUMERIC NOT NULL,\n    last_location_id        INTEGER REFERENCES locations(id),\n    event_id                INTEGER DEFAULT 0 REFERENCES navigation_event_types(event_id),\n    event_description       TEXT\n\n    -- Hint: Use the following query to see event types as strings instead of numbers:\n    --       SELECT * FROM navigation_events_view;\n);\n\nCREATE TABLE navigation_event_types\n(\n    event_id        INTEGER NOT NULL PRIMARY KEY,\n    event_name      TEXT NOT NULL\n);\n\nCREATE TABLE annotated_user_behavior\n(\n    timestamp   NUMERIC NOT NULL,\n    event       INTEGER NOT NULL /* event corresponds to the MNTraceUserBehaviorEvent enum in MNTrace.h. Event types:\n        Unknown = 0\n        Reroute = 1\n        OffRoute = 2\n    */\n);\n\nCREATE TABLE annotated_user_environments\n(\n    start_timestamp     NUMERIC NOT NULL,\n    end_timestamp       NUMERIC NOT NULL,\n    environment_type    INTEGER NOT NULL /* environment_type corresponds to the MNTraceUserEnvironmentType enum in MNTrace.h. Environment types:\n        Unknown = 0\n        UrbanCanyon = 1\n        DeepUrbanCanyon = 2\n        TallTrees = 3\n        Tunnel = 4\n        Overpass = 5\n        Frontage = 6\n        Freeway = 7\n    */\n);\n\nCREATE TABLE navigation_updates\n(\n    timestamp                   NUMERIC,\n    type                        NUMERIC,\n    parameters                  BLOB                  -- NSDictionary specific to parameters based on type of event\n);\n\n-- Custom Route Creation\n\nCREATE TABLE custom_route_creation_actions (\n    request_timestamp       NUMERIC,\n    response_timestamp      NUMERIC,\n    request_data            BLOB,   -- GEODirectionsRequest\n    response_data           BLOB,   -- GEODirectionsResponse\n    response_error_data     BLOB,   -- NSError\n    anchor_points_data      BLOB,   -- NSArray of GEOComposedRouteAnchorPoint\n    action                  INTEGER -- MNRouteEditorAction in MNNavigationEnums.h\n);\n\n-- Views\n\n-- info\n\nCREATE VIEW info_view AS\n    SELECT\n        version,\n        original_version,\n        strftime('%H:%M:%S', time(recording_start_time, 'unixepoch', 'localtime')) AS recording_start_time,\n        strftime('%H:%M:%S', time(directions_start_time, 'unixepoch', 'localtime')) AS directions_start_time,\n        strftime('%H:%M:%S', time(navigation_start_time, 'unixepoch', 'localtime')) AS navigation_start_time,\n        strftime('%H:%M:%S', time(navigation_end_time, 'unixepoch', 'localtime')) AS navigation_end_time,\n        simulation\n    FROM\n        info;\n\n-- directions\n\nCREATE VIEW directions_view AS\n    SELECT\n        id,\n        PRINTF(\"%.3f\", request_timestamp) AS request_time,\n        PRINTF(\"%.3f\", response_timestamp) AS response_time,\n        LENGTH(request_data) AS request,\n        LENGTH(response_data) AS response,\n        LENGTH(response_error_data) AS error,\n        LENGTH(waypoints_data) AS waypoints,\n        selected_route_index\n    FROM\n        directions;\n         \n-- eta_traffic_updates\n\nCREATE VIEW etau_view AS\n    SELECT\n        id,\n        PRINTF(\"%.3f\", request_timestamp) AS request_time,\n        PRINTF(\"%.3f\", response_timestamp) AS response_time,\n        LENGTH(request_data) AS request,\n        LENGTH(response_data) AS response,\n        LENGTH(response_error_data) AS error,\n        destination_name AS destination\n    FROM\n        eta_traffic_updates;\n\n-- navigation_events\n\nCREATE VIEW navigation_events_view AS\n    SELECT\n        PRINTF(\"%.3f\", relative_timestamp) AS relative_time,\n        PRINTF(\"%d\", absolute_timestamp) AS absolute_time,\n        strftime('%H:%M:%S', time(absolute_timestamp, 'unixepoch', 'localtime')) AS time,\n        last_location_id AS location,\n        event_name,\n        event_description\n    FROM\n        navigation_events INNER JOIN navigation_event_types ON navigation_events.event_id = navigation_event_types.event_id;\n\n-- ev_data\n\nCREATE VIEW ev_data_view as\n    SELECT\n        PRINTF(\"%.1f\", relative_timestamp) AS time,\n        strftime('%H:%M:%S', time(absolute_timestamp, 'unixepoch', 'localtime')) AS date,\n        PRINTF(\"%.0f%%\", battery_percentage * 100) AS \"battery%\",\n        PRINTF(\"%.1f\", current_range_m) AS \"range (meters)\",\n        PRINTF(\"%.1f\", current_battery_capacity_kwh) AS \"capacity (kwh)\",\n        is_charging,\n        CASE WHEN length(vehicle_data) > 0 THEN identifier END as identifier\n    FROM\n        ev_data;\n\n-- custom_route_creation_actions\n\nCREATE VIEW route_creation_actions_view AS\n    SELECT\n        rowid AS 'Index',\n        PRINTF(\"%.3f\", request_timestamp) AS 'Request Time',\n        PRINTF(\"%.3f\", response_timestamp) AS 'Response Time',\n        LENGTH(request_data) AS 'Request',\n        LENGTH(response_data) AS 'Response',\n        LENGTH(response_error_data) AS 'Error',\n        LENGTH(anchor_points_data) AS 'Anchor Points',\n        CASE action\n            WHEN 0 THEN 'Unset'\n            WHEN 1 THEN 'Append Anchor'\n            WHEN 2 THEN 'Delete Anchor'\n            WHEN 101 THEN 'Reverse'\n            WHEN 102 THEN 'Out and Back'\n            WHEN 103 THEN 'Close Loop'\n            WHEN 1001 THEN 'Undo'\n            WHEN 1002 THEN 'Redo'\n            ELSE 'Unknown'\n        END AS 'Action'\n    FROM\n        custom_route_creation_actions;\n"
- "\x11#"
- "\x15\x13"
- "%0.2fs (%d)"
- "Assertion failed: _route != ((void *)0)"
- "Assertion failed: finishedHandler != ((void *)0)"
- "Error updating location ID for navigation event"
- "INSERT INTO navigation_events (relative_timestamp, absolute_timestamp, last_location_id, event_id, event_description) VALUES (?, ?, ?, ?, ?)"
- "Insufficient space allocated to copy string contents"
- "Location does not have ID"
- "Navigation/MNTraceSchema.swift"
- "Removed trace \"%@\" because it is too old."
- "SELECT relative_timestamp, absolute_timestamp, last_location_id, event_name, event_description, navigation_events.event_id FROM navigation_events INNER JOIN navigation_event_types ON navigation_events.event_id = navigation_event_types.event_id"
- "Should have been handled above"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "TQ,N,V_locationID"
- "UPDATE navigation_events SET last_location_id = ? WHERE rowid = ?"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "_eventsPendingLocationReference"
- "_locationID"
- "_trackedBannerIDs"
- "_updateNavigationEventLocationID"
- "_updateNavigationEventsWithLocationReference:"
- "earlierDate:"
- "invalid Collection: less than 'count' elements in collection"
- "location.traceIndex != NSNotFound"
- "locationID"
- "recordNavigationEvent:forLocation:description:"
- "setLocationID:"
- "v40@0:8q16@24@32"

```
