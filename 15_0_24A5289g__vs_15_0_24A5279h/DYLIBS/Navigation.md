## Navigation

> `/System/Library/PrivateFrameworks/Navigation.framework/Versions/A/Navigation`

```diff

-2334.20.6.20.1
-  __TEXT.__text: 0xeaf8c
+2332.20.6.6.1
+  __TEXT.__text: 0xe9fa4
   __TEXT.__auth_stubs: 0x1240
-  __TEXT.__objc_methlist: 0xe3f8
-  __TEXT.__cstring: 0x1732b
+  __TEXT.__objc_methlist: 0xe3f0
+  __TEXT.__cstring: 0x171cd
   __TEXT.__const: 0x6f4
   __TEXT.__constg_swiftt: 0x124
   __TEXT.__swift5_typeref: 0x9b

   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_proto: 0x8
-  __TEXT.__oslogstring: 0xaae8
-  __TEXT.__gcc_except_tab: 0x49cc
-  __TEXT.__ustring: 0x166
-  __TEXT.__unwind_info: 0x39b0
+  __TEXT.__oslogstring: 0xa935
+  __TEXT.__gcc_except_tab: 0x49c8
+  __TEXT.__ustring: 0x15e
+  __TEXT.__unwind_info: 0x3978
   __TEXT.__eh_frame: 0x110
-  __TEXT.__objc_classname: 0x21eb
-  __TEXT.__objc_methname: 0x2494d
-  __TEXT.__objc_methtype: 0x7519
-  __TEXT.__objc_stubs: 0x1bcc0
-  __DATA_CONST.__got: 0xae0
-  __DATA_CONST.__const: 0x5ca8
+  __TEXT.__objc_classname: 0x2209
+  __TEXT.__objc_methname: 0x2493e
+  __TEXT.__objc_methtype: 0x754c
+  __TEXT.__objc_stubs: 0x1bca0
+  __DATA_CONST.__got: 0xad0
+  __DATA_CONST.__const: 0x5b30
   __DATA_CONST.__objc_classlist: 0x728
   __DATA_CONST.__objc_catlist: 0x138
-  __DATA_CONST.__objc_protolist: 0x220
+  __DATA_CONST.__objc_protolist: 0x228
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7d40
+  __DATA_CONST.__objc_selrefs: 0x7d48
   __DATA_CONST.__objc_protorefs: 0xb8
   __DATA_CONST.__objc_superrefs: 0x4c0
   __DATA_CONST.__objc_arraydata: 0x98
   __AUTH_CONST.__auth_got: 0x938
   __AUTH_CONST.__auth_ptr: 0x68
   __AUTH_CONST.__const: 0x25d0
-  __AUTH_CONST.__cfstring: 0xc200
-  __AUTH_CONST.__objc_const: 0x1f020
+  __AUTH_CONST.__cfstring: 0xbde0
+  __AUTH_CONST.__objc_const: 0x1f0a8
   __AUTH_CONST.__objc_intobj: 0x888
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_doubleobj: 0xe0
   __AUTH.__objc_data: 0x22a8
   __AUTH.__data: 0xd8
-  __DATA.__objc_ivar: 0x11ec
-  __DATA.__data: 0x2078
+  __DATA.__objc_ivar: 0x11f0
+  __DATA.__data: 0x20d8
   __DATA.__bss: 0x140
   __DATA.__common: 0x1d0
   __DATA_DIRTY.__objc_ivar: 0x1a8

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5708
-  Symbols:   14282
-  CStrings:  2079
+  Functions: 5702
+  Symbols:   14281
+  CStrings:  2047
 
Symbols:
+ -[GEOComposedRoute(MNExtras) _isNavigableForWatch]
+ -[MNAudioManager audioHardwareEngine:didActivateAudioSession:]
+ -[MNAudioManager audioHardwareEngine:didStartSpeakingPrompt:]
+ -[MNGuidanceARInfo initWithEventType:maneuverType:instruction:variableOverrides:arrowLabel:locationCoordinate:maneuverRoadName:heading:stepIndex:]
+ -[MNGuidanceARInfo initWithEventType:maneuverType:instruction:variableOverrides:arrowLabel:locationCoordinateRange:maneuverRoadName:stepIndex:]
+ -[MNGuidanceManager _notifySpeechEvent:waypointCategory:ignorePromptStyle:]
+ -[MNGuidanceManager _repeatSpokenEvent:]
+ -[MNLocationMatchInfo .cxx_destruct]
+ -[MNLocationMatchInfo initWithMatchQuality:matchCoordinate:matchCourse:matchFormOfWay:matchRoadClass:matchShifted:matchDataArray:]
+ -[MNLocationMatchInfo matchDataArray]
+ OBJC_IVAR_$_MNAudioManager._audioEngine
+ OBJC_IVAR_$_MNLocationMatchInfo._matchDataArray
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MNAudioHardwareEngineObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MNAudioHardwareEngineObserver
+ __OBJC_$_PROTOCOL_REFS_MNAudioHardwareEngineObserver
+ __OBJC_LABEL_PROTOCOL_$_MNAudioHardwareEngineObserver
+ __OBJC_PROTOCOL_$_MNAudioHardwareEngineObserver
+ ___75-[MNGuidanceManager _notifySpeechEvent:waypointCategory:ignorePromptStyle:]_block_invoke
+ _objc_msgSend$_isNavigableForWatch
+ _objc_msgSend$_notifySpeechEvent:waypointCategory:ignorePromptStyle:
+ _objc_msgSend$_repeatSpokenEvent:
+ _objc_msgSend$audioManager:didActivateAudioSession:
+ _objc_msgSend$audioManager:didStartSpeakingPrompt:
+ _objc_msgSend$clearAlEvents
+ _objc_msgSend$forceStop
+ _objc_msgSend$initWithEventType:maneuverType:instruction:variableOverrides:arrowLabel:locationCoordinate:maneuverRoadName:heading:stepIndex:
+ _objc_msgSend$initWithEventType:maneuverType:instruction:variableOverrides:arrowLabel:locationCoordinateRange:maneuverRoadName:stepIndex:
+ _objc_msgSend$initWithMatchQuality:matchCoordinate:matchCourse:matchFormOfWay:matchRoadClass:matchShifted:matchDataArray:
+ _objc_msgSend$speaking
- -[GEOComposedRoute(MNExtras) isNavigableForWatch]
- -[MNGuidanceARInfo guidanceEventID]
- -[MNGuidanceARInfo initWithEventID:type:maneuverType:instruction:variableOverrides:arrowLabel:locationCoordinate:maneuverRoadName:heading:stepIndex:]
- -[MNGuidanceARInfo initWithEventID:type:maneuverType:instruction:variableOverrides:arrowLabel:locationCoordinateRange:maneuverRoadName:stepIndex:]
- -[MNGuidanceManager _announcementStageForEvent:]
- -[MNGuidanceManager _notifySpeechEvent:waypointCategory:startingVariantIndex:ignorePromptStyle:]
- -[MNGuidanceManager _spokenStringForEvent:waypointCategory:]
- -[MNLocation initWithClientLocation:matchInfo:]
- -[MNLocationMatchInfo initWithMatchQuality:matchCoordinate:matchCourse:matchFormOfWay:matchRoadClass:matchShifted:]
- -[MNParkedVehicleDetector _expireVehicleDisconnectSignal]
- -[MNTraceNavigationEventRecorder _descriptionForARInfo:]
- OBJC_IVAR_$_MNGuidanceARInfo._guidanceEventID
- _VirtualGarageConfig_EVRoutingAllowSteppingRoutes
- _VirtualGarageConfig_EVRoutingEnableAllowListing
- ___60-[MNGuidanceManager _spokenStringForEvent:waypointCategory:]_block_invoke
- ___74-[MNTraceNavigationEventRecorder navigationSession:updateSignsWithARInfo:]_block_invoke
- ___96-[MNGuidanceManager _notifySpeechEvent:waypointCategory:startingVariantIndex:ignorePromptStyle:]_block_invoke
- ___block_descriptor_40_e8_32s_e36_"NSString"16?0"MNGuidanceARInfo"8ls32l8
- _objc_msgSend$_announcementStageForEvent:
- _objc_msgSend$_descriptionForARInfo:
- _objc_msgSend$_expireVehicleDisconnectSignal
- _objc_msgSend$_notifySpeechEvent:waypointCategory:startingVariantIndex:ignorePromptStyle:
- _objc_msgSend$_spokenStringForEvent:waypointCategory:
- _objc_msgSend$guidanceEventID
- _objc_msgSend$initWithClientLocation:matchInfo:
- _objc_msgSend$initWithEventID:type:maneuverType:instruction:variableOverrides:arrowLabel:locationCoordinate:maneuverRoadName:heading:stepIndex:
- _objc_msgSend$initWithEventID:type:maneuverType:instruction:variableOverrides:arrowLabel:locationCoordinateRange:maneuverRoadName:stepIndex:
- _objc_msgSend$initWithMatchQuality:matchCoordinate:matchCourse:matchFormOfWay:matchRoadClass:matchShifted:
- _objc_msgSend$isNavigableForWatch
- _objc_msgSend$matchInfo
CStrings:
+ "\nCREATE TABLE info\n(\n    -- 0: Navigation\n    -- 1: Route Planning\n    -- 2: Custom Route Creation\n    trace_type              INTEGER NOT NULL,\n    \n    name                    TEXT,               -- Deprecated and unset\n    version                 INTEGER NOT NULL,\n    recording_start_time    NUMERIC,            -- All relative timestamps in other tables are relative to this time.\n    directions_start_time   NUMERIC,            -- The time of the first directions request. This is approximately the time when\n                                                -- the user entered route preview, but not exactly. Additionally, when multiple\n                                                -- directions requests are made in route preview (i.e. multi-stop routes) this will\n                                                -- be the time of the last request.\n    navigation_start_time   NUMERIC,            -- This is typically the same as `recording_start_time` (though not guaranteed in future versions)\n    navigation_end_time     NUMERIC,\n    start_time              INTEGER,            -- Deprecated and unset, use start_directions_time or start_navigation_time instead\n    end_time                INTEGER,            -- Deprecated and unset, use end_navigation_time instead\n    start_data              BLOB,               -- Deprecated and unset, use waypoints_data in directions table instead\n    end_data                BLOB,               -- Deprecated and unset, use waypoints_data in directions table instead\n    simulation              INTEGER,\n    route_genius            INTEGER,            -- Deprecated and unset, we don't record navtraces for Route Genius\n    cl_mapmatch             INTEGER,            -- Deprecated and unset, as of Azul this will always be true\n    original_version        INTEGER,\n    initial_course          NUMERIC,            -- Deprecated and unset, use course in locations table instead\n    directions_url          TEXT\n);\n\nCREATE TABLE environment_info\n(\n    name    TEXT NOT NULL,\n    value   TEXT NOT NULL\n);\n\nCREATE TABLE debug_settings\n(\n    setting_name    TEXT,\n    setting_value   TEXT\n);\n\nCREATE TABLE audio_settings\n(\n    db_timestamp        NUMERIC NOT NULL,\n    pause_spoken_audio  INTEGER,\n    volume_setting      INTEGER\n);\n\nCREATE TABLE misc_info\n(\n    key     TEXT NOT NULL,\n    value   NOT NULL        -- Type intentionally unspecified. This column can support multiple types.\n);\n\nCREATE TABLE bookmarks\n(\n    id                  INTEGER PRIMARY KEY ASC AUTOINCREMENT,\n    timestamp           NUMERIC NOT NULL,\n    screenshot_data     BLOB            -- PNG screenshot\n);\n\nCREATE TABLE stylesheets\n(\n    id                  INTEGER PRIMARY KEY ASC AUTOINCREMENT,\n    stylesheet_name     TEXT,\n    stylesheet_data     BLOB\n);\n        \nCREATE TABLE locations\n(\n    id                      INTEGER PRIMARY KEY ASC AUTOINCREMENT,\n    db_timestamp            NUMERIC NOT NULL,\n    cl_timestamp            NUMERIC,\n    latitude                NUMERIC,\n    longitude               NUMERIC,\n    raw_latitude            NUMERIC,\n    raw_longitude           NUMERIC,\n    horizontal_accuracy     NUMERIC,\n    vertical_accuracy       NUMERIC,\n    altitude                NUMERIC,\n    speed                   NUMERIC,\n    speed_accuracy          NUMERIC,\n    course                  NUMERIC,\n    raw_course              NUMERIC,\n    course_accuracy         NUMERIC,\n    type                    INTEGER,    -- CLLocationType in CLLocationType_Private.h\n    reference_frame         INTEGER,    -- CLClientLocationReferenceFrame in CLClientTypes.h\n    raw_reference_frame     INTEGER,    -- CLClientLocationReferenceFrame in CLClientTypes.h\n    error_data              BLOB,       -- PB Serialized NSError\n    event_type              INTEGER,\n    corrected_latitude      NUMERIC,\n    corrected_longitude     NUMERIC,\n    corrected_course        NUMERIC,\n    match_type              NUMERIC,\n    active_transport_type   INTEGER DEFAULT 4, -- default is the unknown transport type\n    match_info_quality      INTEGER,\n    match_info_latitude     NUMERIC,\n    match_info_longitude    NUMERIC,\n    match_info_course       NUMERIC,\n    match_info_form_of_way  INTEGER,\n    match_info_road_class   INTEGER,\n    match_info_shifted      INTEGER,\n    match_info_data_array   BLOB,\n    speed_limit             INTEGER,\n    shield_text             TEXT,\n    shield_type             INTEGER\n);\n\nCREATE TABLE location_match_info\n(\n    location_id                     INTEGER REFERENCES locations(id),\n    route_coordinate                NUMERIC,\n    step_index                      INTEGER,\n    form_of_way                     INTEGER,\n    route_match_score               NUMERIC,\n    distance_from_route             NUMERIC,\n    max_route_distance              NUMERIC,\n    route_distance_match_score      NUMERIC,\n    route_distance_weight           NUMERIC,\n    route_course_delta              NUMERIC,\n    max_route_course_delta          NUMERIC,\n    route_course_match_score        NUMERIC,\n    route_course_weight             NUMERIC,\n    road_width_on_route             NUMERIC,\n    distance_from_road              NUMERIC,\n    road_course_delta               NUMERIC,\n    distance_from_nearest_junction  NUMERIC\n);\n\nCREATE TABLE directions\n(\n    id                      INTEGER PRIMARY KEY ASC AUTOINCREMENT,\n    request_timestamp       NUMERIC,\n    response_timestamp      NUMERIC,\n    request_data            BLOB,               -- PB Serialized GEODirectionsRequest\n    response_data           BLOB,               -- PB Serialized GEODirectionsResponse\n    response_error_data     BLOB,               -- PB Serialized NSError\n    waypoints_data          BLOB,               -- NSArray of GEOComposedWaypoint\n    selected_route_index    INTEGER DEFAULT 0\n);\n\nCREATE TABLE eta_traffic_updates\n(\n    id                      INTEGER PRIMARY KEY ASC AUTOINCREMENT,\n    request_timestamp       NUMERIC NOT NULL,\n    response_timestamp      NUMERIC,\n    request_data            BLOB NOT NULL,  -- PB Serialized\n    response_data           BLOB,           -- PB Serialized\n    response_error_data     BLOB,           -- PB Serialized NSError\n    destination_name        TEXT,\n    dodgeball_alert_type    NUMERIC         -- 0 = Blockage, 1 = Incident, 2 = Reroute, blank = None\n);\n\nCREATE TABLE realtime_transit_updates\n(\n    id                      INTEGER PRIMARY KEY ASC AUTOINCREMENT,\n    timestamp               NUMERIC NOT NULL,\n    request_data            BLOB,           -- PB Serialized\n    response_data           BLOB,           -- PB Serialized\n    response_error_data     BLOB            -- PB Serialized NSError\n);\n\nCREATE TABLE vehicle_speed_data\n(\n    relative_timestamp  NUMERIC NOT NULL,\n    absolute_timestamp  NUMERIC NOT NULL,\n    speed               NUMERIC NOT NULL\n);\n\nCREATE TABLE vehicle_heading_data\n(\n    relative_timestamp  NUMERIC NOT NULL,\n    absolute_timestamp  NUMERIC NOT NULL,\n    heading             NUMERIC NOT NULL\n);\n\nCREATE TABLE motion_data\n(\n    relative_timestamp  NUMERIC NOT NULL,\n    absolute_timestamp  NUMERIC NOT NULL,\n    type                INTEGER,\n    exit_type           INTEGER,\n    confidence          INTEGER\n);\n\nCREATE TABLE compass_heading_data\n(\n    relative_timestamp  NUMERIC NOT NULL,\n    absolute_timestamp  NUMERIC NOT NULL,\n    true_heading        NUMERIC,\n    magnetic_heading    NUMERIC,\n    accuracy            NUMERIC\n);\n\nCREATE TABLE ev_data\n(\n    relative_timestamp              NUMERIC NOT NULL,\n    absolute_timestamp              NUMERIC NOT NULL,\n    identifier                      TEXT,\n    current_range_m                 NUMERIC,\n    max_range_m                     NUMERIC,\n    battery_percentage              NUMERIC,\n    min_battery_capacity_kwh        NUMERIC,\n    current_battery_capacity_kwh    NUMERIC,\n    max_battery_capacity_kwh        NUMERIC,\n    consumption_arguments           TEXT,\n    charging_arguments              TEXT,\n    is_charging                     NUMERIC,\n    active_connector                NUMERIC,\n    vehicle_state_origin            NUMERIC,\n    vehicle_data                    BLOB -- Serialized VGVehicle\n);\n\nCREATE TABLE navigation_events\n(\n    relative_timestamp      NUMERIC NOT NULL,\n    absolute_timestamp      NUMERIC NOT NULL,\n    last_location_id        INTEGER REFERENCES locations(id),\n    event_id                INTEGER DEFAULT 0 REFERENCES navigation_event_types(event_id),\n    event_description       TEXT\n\n    -- Hint: Use the following query to see event types as strings instead of numbers:\n    --       SELECT * FROM navigation_events_view;\n);\n\nCREATE TABLE navigation_event_types\n(\n    event_id        INTEGER NOT NULL PRIMARY KEY,\n    event_name      TEXT NOT NULL\n);\n\nCREATE TABLE annotated_user_behavior\n(\n    timestamp   NUMERIC NOT NULL,\n    event       INTEGER NOT NULL /* event corresponds to the MNTraceUserBehaviorEvent enum in MNTrace.h. Event types:\n        Unknown = 0\n        Reroute = 1\n        OffRoute = 2\n    */\n);\n\nCREATE TABLE annotated_user_environments\n(\n    start_timestamp     NUMERIC NOT NULL,\n    end_timestamp       NUMERIC NOT NULL,\n    environment_type    INTEGER NOT NULL /* environment_type corresponds to the MNTraceUserEnvironmentType enum in MNTrace.h. Environment types:\n        Unknown = 0\n        UrbanCanyon = 1\n        DeepUrbanCanyon = 2\n        TallTrees = 3\n        Tunnel = 4\n        Overpass = 5\n        Frontage = 6\n        Freeway = 7\n    */\n);\n\nCREATE TABLE navigation_updates\n(\n    timestamp                   NUMERIC,\n    type                        NUMERIC,\n    parameters                  BLOB                  -- NSDictionary specific to parameters based on type of event\n);\n\n-- Custom Route Creation\n\nCREATE TABLE custom_route_creation_actions (\n    request_timestamp       NUMERIC,\n    response_timestamp      NUMERIC,\n    request_data            BLOB,   -- GEODirectionsRequest\n    response_data           BLOB,   -- GEODirectionsResponse\n    response_error_data     BLOB,   -- NSError\n    anchor_points_data      BLOB,   -- NSArray of GEOComposedRouteAnchorPoint\n    action                  INTEGER -- MNRouteEditorAction in MNNavigationEnums.h\n);\n\n-- Views\n\n-- info\n\nCREATE VIEW info_view AS\n    SELECT\n        version,\n        original_version,\n        strftime('%!H(MISSING):%!M(MISSING):%!S(MISSING)', time(recording_start_time, 'unixepoch', 'localtime')) AS recording_start_time,\n        strftime('%!H(MISSING):%!M(MISSING):%!S(MISSING)', time(directions_start_time, 'unixepoch', 'localtime')) AS directions_start_time,\n        strftime('%!H(MISSING):%!M(MISSING):%!S(MISSING)', time(navigation_start_time, 'unixepoch', 'localtime')) AS navigation_start_time,\n        strftime('%!H(MISSING):%!M(MISSING):%!S(MISSING)', time(navigation_end_time, 'unixepoch', 'localtime')) AS navigation_end_time,\n        simulation\n    FROM\n        info;\n\n-- directions\n\nCREATE VIEW directions_view AS\n    SELECT\n        id,\n        PRINTF(\"%!f(MISSING)\", request_timestamp) AS request_time,\n        PRINTF(\"%!f(MISSING)\", response_timestamp) AS response_time,\n        LENGTH(request_data) AS request,\n        LENGTH(response_data) AS response,\n        LENGTH(response_error_data) AS error,\n        LENGTH(waypoints_data) AS waypoints,\n        selected_route_index\n    FROM\n        directions;\n         \n-- eta_traffic_updates\n\nCREATE VIEW etau_view AS\n    SELECT\n        id,\n        PRINTF(\"%!f(MISSING)\", request_timestamp) AS request_time,\n        PRINTF(\"%!f(MISSING)\", response_timestamp) AS response_time,\n        LENGTH(request_data) AS request,\n        LENGTH(response_data) AS response,\n        LENGTH(response_error_data) AS error,\n        destination_name AS destination\n    FROM\n        eta_traffic_updates;\n\n-- navigation_events\n\nCREATE VIEW navigation_events_view AS\n    SELECT\n        PRINTF(\"%!f(MISSING)\", relative_timestamp) AS relative_time,\n        PRINTF(\"%!d(MISSING)\", absolute_timestamp) AS absolute_time,\n        strftime('%!H(MISSING):%!M(MISSING):%!S(MISSING)', time(absolute_timestamp, 'unixepoch', 'localtime')) AS time,\n        last_location_id AS location,\n        event_name,\n        event_description\n    FROM\n        navigation_events INNER JOIN navigation_event_types ON navigation_events.event_id = navigation_event_types.event_id;\n\n-- ev_data\n\nCREATE VIEW ev_data_view as\n    SELECT\n        PRINTF(\"%!f(MISSING)\", relative_timestamp) AS time,\n        strftime('%!H(MISSING):%!M(MISSING):%!S(MISSING)', time(absolute_timestamp, 'unixepoch', 'localtime')) AS date,\n        PRINTF(\"%!f(MISSING)%\", battery_percentage * 100) AS \"battery%!\(MISSING)",\n        PRINTF(\"%!f(MISSING)\", current_range_m) AS \"range (meters)\",\n        PRINTF(\"%!f(MISSING)\", current_battery_capacity_kwh) AS \"capacity (kwh)\",\n        is_charging,\n        CASE WHEN length(vehicle_data) > 0 THEN identifier END as identifier\n    FROM\n        ev_data;\n\n-- custom_route_creation_actions\n\nCREATE VIEW route_creation_actions_view AS\n    SELECT\n        rowid AS 'Index',\n        PRINTF(\"%!f(MISSING)\", request_timestamp) AS 'Request Time',\n        PRINTF(\"%!f(MISSING)\", response_timestamp) AS 'Response Time',\n        LENGTH(request_data) AS 'Request',\n        LENGTH(response_data) AS 'Response',\n        LENGTH(response_error_data) AS 'Error',\n        LENGTH(anchor_points_data) AS 'Anchor Points',\n        CASE action\n            WHEN 0 THEN 'Unset'\n            WHEN 1 THEN 'Append Anchor'\n            WHEN 2 THEN 'Delete Anchor'\n            WHEN 101 THEN 'Reverse'\n            WHEN 102 THEN 'Out and Back'\n            WHEN 103 THEN 'Close Loop'\n            WHEN 1001 THEN 'Undo'\n            WHEN 1002 THEN 'Redo'\n            ELSE 'Unknown'\n        END AS 'Action'\n    FROM\n        custom_route_creation_actions;\n"
+ "-[MNGuidanceManager updateSessionStateForReroute:reason:location:]"
+ "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Navigation/Extras/GEOComposedRoute+MNExtras.mm"
+ "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Navigation/Extras/GEOComposedWaypoint+MNExtras.m"
+ "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Navigation/Extras/GEORouteAttributes+MNExtras.m"
+ "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Navigation/Extras/MNSequence.m"
+ "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Navigation/Extras/NSString+MNExtras.m"
+ "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Navigation/Guidance/MNAnnouncementPlanEvent.m"
+ "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Navigation/Instructions/MNInstructions.m"
+ "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Navigation/Instructions/MNTransitInstruction.m"
+ "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Navigation/Interfaces/MNNavigationService.m"
+ "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Navigation/Location/LocationTracking/MNAlternateRoutesUpdater.m"
+ "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Navigation/Location/LocationTracking/MNDepartureUpdater.m"
+ "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Navigation/Location/LocationTracking/MNLocationTracker.m"
+ "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Navigation/Location/LocationTracking/MNTrafficIncidentAlertUpdater.m"
+ "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Navigation/Location/LocationTracking/MNTransitLocationTracker.m"
+ "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Navigation/Location/LocationTracking/MNTunnelLocationProjector.m"
+ "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Navigation/Location/LocationTracking/MNTurnByTurnLocationTracker.mm"
+ "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Navigation/Location/MNCoreLocationProvider.m"
+ "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Navigation/Location/MNLocation.m"
+ "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Navigation/Location/MNLocationManager.m"
+ "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Navigation/Misc/MNNotificationManager.m"
+ "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Navigation/Misc/MNRouteDivergenceFinder.mm"
+ "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Navigation/Misc/MNRouteProximitySensor.m"
+ "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Navigation/Navigation Service Internal/MNNavigationService+CallbackHandling.m"
+ "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Navigation/NavigationState/MNNavigationState.m"
+ "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Navigation/NavigationState/MNNavigationStateGuidance.m"
+ "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Navigation/NavigationState/MNNavigationStateManager.m"
+ "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Navigation/Session/MNDirectionsRequestManager.m"
+ "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Navigation/Session/MNNavigationDetails.m"
+ "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Navigation/Session/MNNavigationProxyUpdater.m"
+ "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Navigation/Session/MNNavigationServer.m"
+ "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Navigation/Session/MNNavigationServiceRemoteProxy.m"
+ "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Navigation/Session/MNNavigationSession.m"
+ "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Navigation/Session/MNNavigationSessionManager.m"
+ "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Navigation/Session/MNRouteManager.m"
+ "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Navigation/Session/MNSessionUpdateManager.m"
+ "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Navigation/Simulation/MNSimulatedLocationGenerator.m"
+ "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Navigation/Traces/MNNavigationTraceManager.m"
+ "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Navigation/Traces/MNTracePlayerTimelineStream.m"
+ "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Navigation/Traces/MNTraceRecorder.m"
+ "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Navigation/TrafficETA/MNDisplayETAInfo.m"
+ "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Navigation/TrafficETA/MNTimeAndDistanceUpdater.m"
+ "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Navigation/TrafficETA/MNTrafficIncidentAlert.m"
+ "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Navigation/TrafficETA/MNTrafficIncidentTriggerPoint.m"
+ "Could not get upgrade schema."
+ "INSERT INTO locations (db_timestamp, cl_timestamp, latitude, longitude, raw_latitude, raw_longitude, horizontal_accuracy, vertical_accuracy, altitude, speed, speed_accuracy, course, raw_course, course_accuracy, type, reference_frame, raw_reference_frame, event_type, corrected_latitude, corrected_longitude, corrected_course, match_type, active_transport_type, speed_limit, shield_text, shield_type, match_info_quality, match_info_latitude, match_info_longitude, match_info_course, match_info_form_of_way, match_info_road_class, match_info_shifted, match_info_data_array) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
+ "SELECT db_timestamp, cl_timestamp, latitude, longitude, raw_latitude, raw_longitude, horizontal_accuracy, vertical_accuracy, altitude, speed, speed_accuracy, course, raw_course, course_accuracy, type, reference_frame, raw_reference_frame, error_data, event_type, match_info_quality, match_info_latitude, match_info_longitude, match_info_course, match_info_form_of_way, match_info_road_class, match_info_shifted, match_info_data_array, match_type FROM locations"
+ "SELECT db_timestamp, cl_timestamp, latitude, longitude, raw_latitude, raw_longitude, horizontal_accuracy, vertical_accuracy, altitude, speed, speed_accuracy, course, raw_course, course_accuracy, type, reference_frame, raw_reference_frame, error_data, event_type, match_info_quality, match_info_latitude, match_info_longitude, match_info_course, match_info_form_of_way, match_info_road_class, match_info_shifted, match_info_data_array, match_type, corrected_latitude, corrected_longitude, corrected_course FROM locations"
- "\nCREATE TABLE info\n(\n    -- 0: Navigation\n    -- 1: Route Planning\n    -- 2: Custom Route Creation\n    trace_type              INTEGER NOT NULL,\n    \n    name                    TEXT,               -- Deprecated and unset\n    version                 INTEGER NOT NULL,\n    recording_start_time    NUMERIC,            -- All relative timestamps in other tables are relative to this time.\n    directions_start_time   NUMERIC,            -- The time of the first directions request. This is approximately the time when\n                                                -- the user entered route preview, but not exactly. Additionally, when multiple\n                                                -- directions requests are made in route preview (i.e. multi-stop routes) this will\n                                                -- be the time of the last request.\n    navigation_start_time   NUMERIC,            -- This is typically the same as `recording_start_time` (though not guaranteed in future versions)\n    navigation_end_time     NUMERIC,\n    start_time              INTEGER,            -- Deprecated and unset, use start_directions_time or start_navigation_time instead\n    end_time                INTEGER,            -- Deprecated and unset, use end_navigation_time instead\n    start_data              BLOB,               -- Deprecated and unset, use waypoints_data in directions table instead\n    end_data                BLOB,               -- Deprecated and unset, use waypoints_data in directions table instead\n    simulation              INTEGER,\n    route_genius            INTEGER,            -- Deprecated and unset, we don't record navtraces for Route Genius\n    cl_mapmatch             INTEGER,            -- Deprecated and unset, as of Azul this will always be true\n    original_version        INTEGER,\n    initial_course          NUMERIC,            -- Deprecated and unset, use course in locations table instead\n    directions_url          TEXT\n);\n\nCREATE TABLE environment_info\n(\n    name    TEXT NOT NULL,\n    value   TEXT NOT NULL\n);\n\nCREATE TABLE debug_settings\n(\n    setting_name    TEXT,\n    setting_value   TEXT\n);\n\nCREATE TABLE audio_settings\n(\n    db_timestamp        NUMERIC NOT NULL,\n    pause_spoken_audio  INTEGER,\n    volume_setting      INTEGER\n);\n\nCREATE TABLE misc_info\n(\n    key     TEXT NOT NULL,\n    value   NOT NULL        -- Type intentionally unspecified. This column can support multiple types.\n);\n\nCREATE TABLE bookmarks\n(\n    id                  INTEGER PRIMARY KEY ASC AUTOINCREMENT,\n    timestamp           NUMERIC NOT NULL,\n    screenshot_data     BLOB            -- PNG screenshot\n);\n\nCREATE TABLE stylesheets\n(\n    id                  INTEGER PRIMARY KEY ASC AUTOINCREMENT,\n    stylesheet_name     TEXT,\n    stylesheet_data     BLOB\n);\n        \nCREATE TABLE locations\n(\n    id                      INTEGER PRIMARY KEY ASC AUTOINCREMENT,\n    db_timestamp            NUMERIC NOT NULL,\n    cl_timestamp            NUMERIC,\n    latitude                NUMERIC,\n    longitude               NUMERIC,\n    raw_latitude            NUMERIC,\n    raw_longitude           NUMERIC,\n    horizontal_accuracy     NUMERIC,\n    vertical_accuracy       NUMERIC,\n    altitude                NUMERIC,\n    speed                   NUMERIC,\n    speed_accuracy          NUMERIC,\n    course                  NUMERIC,\n    raw_course              NUMERIC,\n    course_accuracy         NUMERIC,\n    type                    INTEGER,    -- CLLocationType in CLLocationType_Private.h\n    reference_frame         INTEGER,    -- CLClientLocationReferenceFrame in CLClientTypes.h\n    raw_reference_frame     INTEGER,    -- CLClientLocationReferenceFrame in CLClientTypes.h\n    error_data              BLOB,       -- PB Serialized NSError\n    event_type              INTEGER,\n    corrected_latitude      NUMERIC,\n    corrected_longitude     NUMERIC,\n    corrected_course        NUMERIC,\n    match_type              NUMERIC,\n    active_transport_type   INTEGER DEFAULT 4, -- default is the unknown transport type\n    match_info_quality      INTEGER,\n    match_info_latitude     NUMERIC,\n    match_info_longitude    NUMERIC,\n    match_info_course       NUMERIC,\n    match_info_form_of_way  INTEGER,\n    match_info_road_class   INTEGER,\n    match_info_shifted      INTEGER,\n    speed_limit             INTEGER,\n    shield_text             TEXT,\n    shield_type             INTEGER\n);\n\nCREATE TABLE location_match_info\n(\n    location_id                     INTEGER REFERENCES locations(id),\n    route_coordinate                NUMERIC,\n    step_index                      INTEGER,\n    form_of_way                     INTEGER,\n    route_match_score               NUMERIC,\n    distance_from_route             NUMERIC,\n    max_route_distance              NUMERIC,\n    route_distance_match_score      NUMERIC,\n    route_distance_weight           NUMERIC,\n    route_course_delta              NUMERIC,\n    max_route_course_delta          NUMERIC,\n    route_course_match_score        NUMERIC,\n    route_course_weight             NUMERIC,\n    road_width_on_route             NUMERIC,\n    distance_from_road              NUMERIC,\n    road_course_delta               NUMERIC,\n    distance_from_nearest_junction  NUMERIC\n);\n\nCREATE TABLE directions\n(\n    id                      INTEGER PRIMARY KEY ASC AUTOINCREMENT,\n    request_timestamp       NUMERIC,\n    response_timestamp      NUMERIC,\n    request_data            BLOB,               -- PB Serialized GEODirectionsRequest\n    response_data           BLOB,               -- PB Serialized GEODirectionsResponse\n    response_error_data     BLOB,               -- PB Serialized NSError\n    waypoints_data          BLOB,               -- NSArray of GEOComposedWaypoint\n    selected_route_index    INTEGER DEFAULT 0\n);\n\nCREATE TABLE eta_traffic_updates\n(\n    id                      INTEGER PRIMARY KEY ASC AUTOINCREMENT,\n    request_timestamp       NUMERIC NOT NULL,\n    response_timestamp      NUMERIC,\n    request_data            BLOB NOT NULL,  -- PB Serialized\n    response_data           BLOB,           -- PB Serialized\n    response_error_data     BLOB,           -- PB Serialized NSError\n    destination_name        TEXT,\n    dodgeball_alert_type    NUMERIC         -- 0 = Blockage, 1 = Incident, 2 = Reroute, blank = None\n);\n\nCREATE TABLE realtime_transit_updates\n(\n    id                      INTEGER PRIMARY KEY ASC AUTOINCREMENT,\n    timestamp               NUMERIC NOT NULL,\n    request_data            BLOB,           -- PB Serialized\n    response_data           BLOB,           -- PB Serialized\n    response_error_data     BLOB            -- PB Serialized NSError\n);\n\nCREATE TABLE vehicle_speed_data\n(\n    relative_timestamp  NUMERIC NOT NULL,\n    absolute_timestamp  NUMERIC NOT NULL,\n    speed               NUMERIC NOT NULL\n);\n\nCREATE TABLE vehicle_heading_data\n(\n    relative_timestamp  NUMERIC NOT NULL,\n    absolute_timestamp  NUMERIC NOT NULL,\n    heading             NUMERIC NOT NULL\n);\n\nCREATE TABLE motion_data\n(\n    relative_timestamp  NUMERIC NOT NULL,\n    absolute_timestamp  NUMERIC NOT NULL,\n    type                INTEGER,\n    exit_type           INTEGER,\n    confidence          INTEGER\n);\n\nCREATE TABLE compass_heading_data\n(\n    relative_timestamp  NUMERIC NOT NULL,\n    absolute_timestamp  NUMERIC NOT NULL,\n    true_heading        NUMERIC,\n    magnetic_heading    NUMERIC,\n    accuracy            NUMERIC\n);\n\nCREATE TABLE ev_data\n(\n    relative_timestamp              NUMERIC NOT NULL,\n    absolute_timestamp              NUMERIC NOT NULL,\n    identifier                      TEXT,\n    current_range_m                 NUMERIC,\n    max_range_m                     NUMERIC,\n    battery_percentage              NUMERIC,\n    min_battery_capacity_kwh        NUMERIC,\n    current_battery_capacity_kwh    NUMERIC,\n    max_battery_capacity_kwh        NUMERIC,\n    consumption_arguments           TEXT,\n    charging_arguments              TEXT,\n    is_charging                     NUMERIC,\n    active_connector                NUMERIC,\n    vehicle_state_origin            NUMERIC,\n    vehicle_data                    BLOB -- Serialized VGVehicle\n);\n\nCREATE TABLE navigation_events\n(\n    relative_timestamp      NUMERIC NOT NULL,\n    absolute_timestamp      NUMERIC NOT NULL,\n    last_location_id        INTEGER REFERENCES locations(id),\n    event_id                INTEGER DEFAULT 0 REFERENCES navigation_event_types(event_id),\n    event_description       TEXT\n\n    -- Hint: Use the following query to see event types as strings instead of numbers:\n    --       SELECT * FROM navigation_events_view;\n);\n\nCREATE TABLE navigation_event_types\n(\n    event_id        INTEGER NOT NULL PRIMARY KEY,\n    event_name      TEXT NOT NULL\n);\n\nCREATE TABLE annotated_user_behavior\n(\n    timestamp   NUMERIC NOT NULL,\n    event       INTEGER NOT NULL /* event corresponds to the MNTraceUserBehaviorEvent enum in MNTrace.h. Event types:\n        Unknown = 0\n        Reroute = 1\n        OffRoute = 2\n    */\n);\n\nCREATE TABLE annotated_user_environments\n(\n    start_timestamp     NUMERIC NOT NULL,\n    end_timestamp       NUMERIC NOT NULL,\n    environment_type    INTEGER NOT NULL /* environment_type corresponds to the MNTraceUserEnvironmentType enum in MNTrace.h. Environment types:\n        Unknown = 0\n        UrbanCanyon = 1\n        DeepUrbanCanyon = 2\n        TallTrees = 3\n        Tunnel = 4\n        Overpass = 5\n        Frontage = 6\n        Freeway = 7\n    */\n);\n\nCREATE TABLE navigation_updates\n(\n    timestamp                   NUMERIC,\n    type                        NUMERIC,\n    parameters                  BLOB                  -- NSDictionary specific to parameters based on type of event\n);\n\n-- Custom Route Creation\n\nCREATE TABLE custom_route_creation_actions (\n    request_timestamp       NUMERIC,\n    response_timestamp      NUMERIC,\n    request_data            BLOB,   -- GEODirectionsRequest\n    response_data           BLOB,   -- GEODirectionsResponse\n    response_error_data     BLOB,   -- NSError\n    anchor_points_data      BLOB,   -- NSArray of GEOComposedRouteAnchorPoint\n    action                  INTEGER -- MNRouteEditorAction in MNNavigationEnums.h\n);\n\n-- Views\n\n-- info\n\nCREATE VIEW info_view AS\n    SELECT\n        version,\n        original_version,\n        strftime('%!H(MISSING):%!M(MISSING):%!S(MISSING)', time(recording_start_time, 'unixepoch', 'localtime')) AS recording_start_time,\n        strftime('%!H(MISSING):%!M(MISSING):%!S(MISSING)', time(directions_start_time, 'unixepoch', 'localtime')) AS directions_start_time,\n        strftime('%!H(MISSING):%!M(MISSING):%!S(MISSING)', time(navigation_start_time, 'unixepoch', 'localtime')) AS navigation_start_time,\n        strftime('%!H(MISSING):%!M(MISSING):%!S(MISSING)', time(navigation_end_time, 'unixepoch', 'localtime')) AS navigation_end_time,\n        simulation\n    FROM\n        info;\n\n-- directions\n\nCREATE VIEW directions_view AS\n    SELECT\n        id,\n        PRINTF(\"%!f(MISSING)\", request_timestamp) AS request_time,\n        PRINTF(\"%!f(MISSING)\", response_timestamp) AS response_time,\n        LENGTH(request_data) AS request,\n        LENGTH(response_data) AS response,\n        LENGTH(response_error_data) AS error,\n        LENGTH(waypoints_data) AS waypoints,\n        selected_route_index\n    FROM\n        directions;\n         \n-- eta_traffic_updates\n\nCREATE VIEW etau_view AS\n    SELECT\n        id,\n        PRINTF(\"%!f(MISSING)\", request_timestamp) AS request_time,\n        PRINTF(\"%!f(MISSING)\", response_timestamp) AS response_time,\n        LENGTH(request_data) AS request,\n        LENGTH(response_data) AS response,\n        LENGTH(response_error_data) AS error,\n        destination_name AS destination\n    FROM\n        eta_traffic_updates;\n\n-- navigation_events\n\nCREATE VIEW navigation_events_view AS\n    SELECT\n        PRINTF(\"%!f(MISSING)\", relative_timestamp) AS relative_time,\n        PRINTF(\"%!d(MISSING)\", absolute_timestamp) AS absolute_time,\n        strftime('%!H(MISSING):%!M(MISSING):%!S(MISSING)', time(absolute_timestamp, 'unixepoch', 'localtime')) AS time,\n        last_location_id AS location,\n        event_name,\n        event_description\n    FROM\n        navigation_events INNER JOIN navigation_event_types ON navigation_events.event_id = navigation_event_types.event_id;\n\n-- ev_data\n\nCREATE VIEW ev_data_view as\n    SELECT\n        PRINTF(\"%!f(MISSING)\", relative_timestamp) AS time,\n        strftime('%!H(MISSING):%!M(MISSING):%!S(MISSING)', time(absolute_timestamp, 'unixepoch', 'localtime')) AS date,\n        PRINTF(\"%!f(MISSING)%\", battery_percentage * 100) AS \"battery%!\(MISSING)",\n        PRINTF(\"%!f(MISSING)\", current_range_m) AS \"range (meters)\",\n        PRINTF(\"%!f(MISSING)\", current_battery_capacity_kwh) AS \"capacity (kwh)\",\n        is_charging,\n        CASE WHEN length(vehicle_data) > 0 THEN identifier END as identifier\n    FROM\n        ev_data;\n\n-- custom_route_creation_actions\n\nCREATE VIEW route_creation_actions_view AS\n    SELECT\n        rowid AS 'Index',\n        PRINTF(\"%!f(MISSING)\", request_timestamp) AS 'Request Time',\n        PRINTF(\"%!f(MISSING)\", response_timestamp) AS 'Response Time',\n        LENGTH(request_data) AS 'Request',\n        LENGTH(response_data) AS 'Response',\n        LENGTH(response_error_data) AS 'Error',\n        LENGTH(anchor_points_data) AS 'Anchor Points',\n        CASE action\n            WHEN 0 THEN 'Unset'\n            WHEN 1 THEN 'Append Anchor'\n            WHEN 2 THEN 'Delete Anchor'\n            WHEN 101 THEN 'Reverse'\n            WHEN 102 THEN 'Out and Back'\n            WHEN 103 THEN 'Close Loop'\n            WHEN 1001 THEN 'Undo'\n            WHEN 1002 THEN 'Redo'\n            ELSE 'Unknown'\n        END AS 'Action'\n    FROM\n        custom_route_creation_actions;\n"
- " (%!@(MISSING))"
- " /// "
- "%!f(MISSING), %!f(MISSING) | %!d(MISSING)m"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/Navigation/Extras/GEOComposedRoute+MNExtras.mm"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/Navigation/Extras/GEOComposedWaypoint+MNExtras.m"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/Navigation/Extras/GEORouteAttributes+MNExtras.m"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/Navigation/Extras/MNSequence.m"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/Navigation/Extras/NSString+MNExtras.m"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/Navigation/Guidance/MNAnnouncementPlanEvent.m"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/Navigation/Instructions/MNInstructions.m"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/Navigation/Instructions/MNTransitInstruction.m"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/Navigation/Interfaces/MNNavigationService.m"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/Navigation/Location/LocationTracking/MNAlternateRoutesUpdater.m"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/Navigation/Location/LocationTracking/MNDepartureUpdater.m"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/Navigation/Location/LocationTracking/MNLocationTracker.m"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/Navigation/Location/LocationTracking/MNTrafficIncidentAlertUpdater.m"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/Navigation/Location/LocationTracking/MNTransitLocationTracker.m"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/Navigation/Location/LocationTracking/MNTunnelLocationProjector.m"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/Navigation/Location/LocationTracking/MNTurnByTurnLocationTracker.mm"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/Navigation/Location/MNCoreLocationProvider.m"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/Navigation/Location/MNLocation.m"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/Navigation/Location/MNLocationManager.m"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/Navigation/Misc/MNNotificationManager.m"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/Navigation/Misc/MNRouteDivergenceFinder.mm"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/Navigation/Misc/MNRouteProximitySensor.m"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/Navigation/Navigation Service Internal/MNNavigationService+CallbackHandling.m"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/Navigation/NavigationState/MNNavigationState.m"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/Navigation/NavigationState/MNNavigationStateGuidance.m"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/Navigation/NavigationState/MNNavigationStateManager.m"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/Navigation/Session/MNDirectionsRequestManager.m"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/Navigation/Session/MNNavigationDetails.m"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/Navigation/Session/MNNavigationProxyUpdater.m"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/Navigation/Session/MNNavigationServer.m"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/Navigation/Session/MNNavigationServiceRemoteProxy.m"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/Navigation/Session/MNNavigationSession.m"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/Navigation/Session/MNNavigationSessionManager.m"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/Navigation/Session/MNRouteManager.m"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/Navigation/Session/MNSessionUpdateManager.m"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/Navigation/Simulation/MNSimulatedLocationGenerator.m"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/Navigation/Traces/MNNavigationTraceManager.m"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/Navigation/Traces/MNTracePlayerTimelineStream.m"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/Navigation/Traces/MNTraceRecorder.m"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/Navigation/TrafficETA/MNDisplayETAInfo.m"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/Navigation/TrafficETA/MNTimeAndDistanceUpdater.m"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/Navigation/TrafficETA/MNTrafficIncidentAlert.m"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/Navigation/TrafficETA/MNTrafficIncidentTriggerPoint.m"
- "@\"NSString\"16@?0@\"MNGuidanceARInfo\"8"
- "ARRIVAL_CHARGING_STATION"
- "CONTINUE"
- "END"
- "EXECUTE"
- "GET_ON_ROUTE"
- "INITIAL"
- "INSERT INTO locations (db_timestamp, cl_timestamp, latitude, longitude, raw_latitude, raw_longitude, horizontal_accuracy, vertical_accuracy, altitude, speed, speed_accuracy, course, raw_course, course_accuracy, type, reference_frame, raw_reference_frame, event_type, corrected_latitude, corrected_longitude, corrected_course, match_type, active_transport_type, speed_limit, shield_text, shield_type, match_info_quality, match_info_latitude, match_info_longitude, match_info_course, match_info_form_of_way, match_info_road_class, match_info_shifted) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
- "LANE_MANEUVER"
- "LANE_MID_STEP"
- "MERGE"
- "PREPARE"
- "PRE_ARRIVAL_MODE_END"
- "RETURN_TO_ROUTE"
- "SELECT db_timestamp, cl_timestamp, latitude, longitude, raw_latitude, raw_longitude, horizontal_accuracy, vertical_accuracy, altitude, speed, speed_accuracy, course, raw_course, course_accuracy, type, reference_frame, raw_reference_frame, error_data, event_type, match_info_quality, match_info_latitude, match_info_longitude, match_info_course, match_info_form_of_way, match_info_road_class, match_info_shifted, match_type FROM locations"
- "SELECT db_timestamp, cl_timestamp, latitude, longitude, raw_latitude, raw_longitude, horizontal_accuracy, vertical_accuracy, altitude, speed, speed_accuracy, course, raw_course, course_accuracy, type, reference_frame, raw_reference_frame, error_data, event_type, match_info_quality, match_info_latitude, match_info_longitude, match_info_course, match_info_form_of_way, match_info_road_class, match_info_shifted, match_type, corrected_latitude, corrected_longitude, corrected_course FROM locations"
- "START"
- "UNKNOWN_GUIDANCE_EVENT_TYPE"
- "WAYPOINT_ADDRESS"
- "WAYPOINT_CONTACT_CUSTOM_LABEL_ADDRESS"
- "WAYPOINT_CONTACT_HOME"
- "WAYPOINT_CONTACT_OTHER"
- "WAYPOINT_CONTACT_SCHOOL"
- "WAYPOINT_CONTACT_WORK"
- "WAYPOINT_CUSTOM"
- "WAYPOINT_HOME"
- "WAYPOINT_PERSON_LOCATION"
- "WAYPOINT_POI"
- "WAYPOINT_SCHOOL"
- "WAYPOINT_UNKNOWN"
- "WAYPOINT_UNSPECIFIED"
- "WAYPOINT_WORK"
- "[%!@(MISSING) | %!@(MISSING)]"
- "_guidanceEventID"

```
