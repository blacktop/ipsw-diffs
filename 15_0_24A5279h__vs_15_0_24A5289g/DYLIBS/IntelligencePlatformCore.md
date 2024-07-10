## IntelligencePlatformCore

> `/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/Versions/A/IntelligencePlatformCore`

```diff

-103.0.1.200.0
-  __TEXT.__text: 0xadebfc
-  __TEXT.__auth_stubs: 0x9c90
-  __TEXT.__objc_methlist: 0x1604
-  __TEXT.__cstring: 0x3f261
-  __TEXT.__swift5_typeref: 0x1b43c
-  __TEXT.__const: 0x635c9
-  __TEXT.__constg_swiftt: 0x20840
-  __TEXT.__swift5_reflstr: 0x2262f
-  __TEXT.__swift5_fieldmd: 0x2358c
-  __TEXT.__swift5_builtin: 0x474
-  __TEXT.__swift5_mpenum: 0x100
-  __TEXT.__swift5_assocty: 0x2a88
-  __TEXT.__swift5_proto: 0x5a1c
-  __TEXT.__swift5_types: 0x1e18
-  __TEXT.__swift5_protos: 0x34c
-  __TEXT.__oslogstring: 0x1ce53
-  __TEXT.__swift5_capture: 0x3974
+106.0.3.0.0
+  __TEXT.__text: 0xae8b80
+  __TEXT.__auth_stubs: 0x9c00
+  __TEXT.__objc_methlist: 0x1678
+  __TEXT.__cstring: 0x422f1
+  __TEXT.__swift5_typeref: 0x1b428
+  __TEXT.__const: 0x63479
+  __TEXT.__constg_swiftt: 0x20a94
+  __TEXT.__swift5_reflstr: 0x22d6f
+  __TEXT.__swift5_fieldmd: 0x23b24
+  __TEXT.__swift5_builtin: 0x49c
+  __TEXT.__swift5_mpenum: 0x154
+  __TEXT.__swift5_assocty: 0x2a40
+  __TEXT.__swift5_proto: 0x59f4
+  __TEXT.__swift5_types: 0x1e50
+  __TEXT.__swift5_protos: 0x35c
+  __TEXT.__oslogstring: 0x1c8d3
+  __TEXT.__swift5_capture: 0x3a04
   __TEXT.__gcc_except_tab: 0x148
   __TEXT.__dlopen_cstrs: 0xc7
-  __TEXT.__unwind_info: 0x27b68
-  __TEXT.__eh_frame: 0x59560
+  __TEXT.__unwind_info: 0x27ba0
+  __TEXT.__eh_frame: 0x5a390
   __TEXT.__objc_classname: 0x4a5
-  __TEXT.__objc_methname: 0x9c0b
-  __TEXT.__objc_methtype: 0x231a
-  __TEXT.__objc_stubs: 0x1120
+  __TEXT.__objc_methname: 0x9cb1
+  __TEXT.__objc_methtype: 0x236b
+  __TEXT.__objc_stubs: 0x1140
   __DATA_CONST.__got: 0x3df8
-  __DATA_CONST.__const: 0x580
+  __DATA_CONST.__const: 0x5a0
   __DATA_CONST.__objc_classlist: 0x1178
   __DATA_CONST.__objc_protolist: 0x240
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x20f8
+  __DATA_CONST.__objc_selrefs: 0x2140
   __DATA_CONST.__objc_protorefs: 0x118
   __DATA_CONST.__objc_superrefs: 0x80
-  __AUTH_CONST.__auth_got: 0x4e58
-  __AUTH_CONST.__auth_ptr: 0x4758
-  __AUTH_CONST.__const: 0x3dfb8
+  __AUTH_CONST.__auth_got: 0x4e10
+  __AUTH_CONST.__auth_ptr: 0x4730
+  __AUTH_CONST.__const: 0x3e600
   __AUTH_CONST.__cfstring: 0x360
-  __AUTH_CONST.__objc_const: 0x2d7a0
-  __AUTH.__objc_data: 0x7828
-  __AUTH.__data: 0x2e6f8
+  __AUTH_CONST.__objc_const: 0x2d9d0
+  __AUTH.__objc_data: 0x76a0
+  __AUTH.__data: 0x2e7a8
   __DATA.__objc_ivar: 0xc4
-  __DATA.__data: 0x1c2a8
-  __DATA.__bss: 0xa0100
-  __DATA.__common: 0x3480
+  __DATA.__data: 0x1c028
+  __DATA.__bss: 0x9f280
+  __DATA.__common: 0x3288
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/AppIntents.framework/Versions/A/AppIntents
   - /System/Library/Frameworks/Combine.framework/Versions/A/Combine

   - /System/Library/PrivateFrameworks/PegasusAPI.framework/Versions/A/PegasusAPI
   - /System/Library/PrivateFrameworks/PegasusKit.framework/Versions/A/PegasusKit
   - /System/Library/PrivateFrameworks/PersonalizationPortrait.framework/Versions/A/PersonalizationPortrait
+  - /System/Library/PrivateFrameworks/PhotoLibraryServices.framework/Versions/A/PhotoLibraryServices
   - /System/Library/PrivateFrameworks/PhotosFormats.framework/Versions/A/PhotosFormats
   - /System/Library/PrivateFrameworks/PowerLog.framework/Versions/A/PowerLog
   - /System/Library/PrivateFrameworks/ProactiveEventTracker.framework/Versions/A/ProactiveEventTracker

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 56155
-  Symbols:   827
-  CStrings:  5489
+  Functions: 56079
+  Symbols:   830
+  CStrings:  5546
 
Symbols:
+ _OBJC_CLASS_$_PLMediaAnalysisServiceRequestAdapter
+ _PHAssetAnalysisCountProcessedKey
+ _PHAssetAnalysisCountTotalAllowedKey
CStrings:
+ "\n    AND\n        sourceIdentifier = "
+ "\n    AND\n        updateType = "
+ "    DELETE FROM\n        computeIfPastSLA\n    WHERE\n        runByTimestamp < ?\n    RETURNING\n        sourceListenerId"
+ "    DELETE FROM\n        computeIfPastSLA\n    WHERE\n        sourceListenerId = ?"
+ "    DELETE FROM\n        debounceSourceAction\n    WHERE\n        sourceId = ?\n    AND\n        sourceListenerId = ?"
+ "    DELETE FROM\n        debounceSourceAction\n    WHERE\n        sourceId = ?\n    RETURNING\n        sourceListenerId"
+ "    DELETE FROM\n        sourceListenerConfig\n    WHERE\n        viewOrderedId = "
+ "    DELETE FROM\n        sourceListenerState\n    WHERE\n        sourceListenerState.sourceListenerId IN\n    (\n        SELECT\n            sls.sourceListenerId\n        FROM\n            sourceListenerState sls\n        JOIN\n            sourceListenerConfig slc\n        ON\n            sls.sourceListenerConfigId == slc.sourceListenerConfigId\n        WHERE\n            slc.viewOrderedId = "
+ "    DELETE FROM\n        updateQueue\n    WHERE\n        schedule = ?\n    AND\n        viewOrderedId = ?"
+ "    DELETE FROM\n        updateQueue\n    WHERE\n        schedule = ?\n    AND\n        viewOrderedId >= ?\n    RETURNING\n        viewOrderedId\n    ORDER BY\n        viewOrderedId\n    LIMIT\n        1"
+ "    DELETE FROM\n        updateQueue\n    WHERE\n        schedule = ?\n    RETURNING\n        viewOrderedId\n    ORDER BY\n        viewOrderedId\n    LIMIT\n        1"
+ "    DELETE FROM\n        viewConfigRecord\n    WHERE\n        id = "
+ "    DELETE FROM\n        viewState\n    WHERE\n        viewOrderedId = "
+ "    INSERT INTO\n        debounceSourceAction\n    SELECT\n        sls.sourceId,\n        sls.sourceListenerId\n    FROM\n        sourceListenerState sls\n    JOIN\n        sourceListenerConfig slc\n    ON\n        sls.sourceListenerConfigId = slc.sourceListenerConfigId\n    WHERE\n        slc.viewOrderedId = ?\n    AND\n        NOT slc.sourceType = ?\n    AND\n        NOT slc.schedule = ?"
+ "    INSERT INTO\n        debounceSourceAction\n    VALUES\n       (?, ?)"
+ "    INSERT INTO\n        scheduleState (schedule, updateState, startView)\n    VALUES\n        (?, ?, 0)"
+ "    INSERT INTO\n        sourceListenerConfig (\n            viewOrderedId,\n            sourceType,\n            configIndex,\n            schedule,\n            computeIfPastSLA,\n            requiredSource,\n            highPriority,\n            rebuildView,\n            fullRebuildOnChange,\n            config\n        )\n    VALUES (\n        "
+ "    INSERT INTO\n        sourceListenerState (\n            sourceListenerConfigId,\n            sourceId,\n            sourceUpdatedTimestamp,\n            runByTimestamp,\n            bookmark\n        )\n    VALUES (\n        "
+ "    INSERT INTO\n        sourceListenerStateFullRebuild (\n            sourceListenerConfigId,\n            sourceId,\n            sourceUpdatedTimestamp,\n            runByTimestamp,\n            bookmark\n        )\n    VALUES (\n        "
+ "    INSERT INTO\n        sourceState(sourceType, sourceIdentifier, updateType, modifiedTimestamp, available)\n    VALUES\n        ("
+ "    INSERT INTO\n        updateQueue\n    SELECT\n        ?,\n        slc.viewOrderedId\n    FROM\n        sourceListenerConfig slc,\n        sourceListenerState sls\n    WHERE\n        sls.sourceListenerConfigId = slc.sourceListenerConfigId\n    AND\n        sls.sourceListenerId = ?"
+ "    INSERT INTO\n        updateQueue\n    SELECT DISTINCT\n        slc.schedule,\n        slc.viewOrderedId\n    FROM\n        sourceListenerConfig slc,\n        viewState vs\n    WHERE\n        slc.viewOrderedId = vs.viewOrderedId\n    AND\n        vs.attemptCount > 0\n    AND\n        slc.computeIfPastSLA"
+ "    INSERT INTO\n        updateQueue\n    VALUES\n       (?, ?)"
+ "    INSERT INTO\n        viewConfigRecord (\n            id,\n            name,\n            configHash,\n            generationType,\n            customType,\n            updateGroup,\n            writeToStream,\n            artifactType,\n            artifactPath,\n            artifactTable,\n            viewUpdateDependencies,\n            viewUpdateDependents,\n            config\n        )\n    VALUES (\n        "
+ "    INSERT INTO\n        viewState (\n            viewOrderedId,\n            enabledStatus,\n            attemptCount,\n            errorMessage,\n            alwaysAvailable,\n            tablesCreated,\n            diffType,\n            bookmark\n        )\n    VALUES (\n        "
+ "    INSERT INTO\n       computeIfPastSLA\n    VALUES\n       (?, ?)"
+ "    SELECT\n        *\n    FROM\n        sourceListenerConfig\n    WHERE\n        sourceListenerConfigId = ?"
+ "    SELECT\n        *\n    FROM\n        sourceListenerConfig\n    WHERE\n        viewOrderedId = "
+ "    SELECT\n        *\n    FROM\n        sourceListenerConfig\n    WHERE\n        viewOrderedId = ?\n    AND\n        sourceType = ?"
+ "    SELECT\n        *\n    FROM\n        sourceListenerState\n    WHERE\n        sourceListenerConfigId = ?"
+ "    SELECT\n        *\n    FROM\n        sourceListenerState\n    WHERE\n        sourceListenerId = ?"
+ "    SELECT\n        *\n    FROM\n        sourceListenerStateFullRebuild\n    WHERE\n        sourceListenerId = ?"
+ "    SELECT\n        *\n    FROM\n        sourceState\n    WHERE\n        sourceId = ?"
+ "    SELECT\n        *\n    FROM\n        sourceState\n    WHERE\n        sourceType = "
+ "    SELECT\n        *\n    FROM\n        viewConfigRecord\n    WHERE\n        id = ?"
+ "    SELECT\n        *\n    FROM\n        viewState\n    WHERE\n        viewOrderedId = ?"
+ "    SELECT\n        1\n    FROM\n        computeIfPastSLA\n    WHERE\n        sourceListenerId = ?"
+ "    SELECT\n        1\n    FROM\n        debounceSourceAction\n    WHERE\n        sourceId = ?\n    AND\n        sourceListenerId = ?"
+ "    SELECT\n        1\n    FROM\n        grdb_migrations\n    WHERE\n        identifier = ?"
+ "    SELECT\n        1\n    FROM\n        sourceListenerConfig slc,\n        sourceListenerState sls,\n        sourceState s\n    WHERE\n        slc.viewOrderedId = ?\n    AND\n        slc.requiredSource\n    AND\n        slc.sourceListenerConfigId = sls.sourceListenerConfigId\n    AND\n        sls.sourceId = s.sourceId\n    AND NOT\n        s.available\n    LIMIT 1"
+ "    SELECT\n        COUNT(*)\n    FROM\n        updateQueue\n    WHERE\n        schedule = ?\n    AND\n        viewOrderedId >= ?"
+ "    SELECT\n        attemptCount\n    FROM\n        viewState\n    WHERE\n        viewOrderedId = ?"
+ "    SELECT\n        id\n    FROM\n        viewConfigRecord\n    WHERE\n        name = ?"
+ "    SELECT\n        id,\n        artifactPath,\n        artifactTable\n    FROM\n        viewConfigRecord\n    WHERE\n        name = "
+ "    SELECT\n        id,\n        name\n    FROM\n        viewConfigRecord\n    ORDER BY\n        id"
+ "    SELECT\n        id, name\n    FROM\n        viewConfigRecord\n    WHERE\n        updateGroup = ?"
+ "    SELECT\n        name,\n        artifactPath,\n        artifactTable\n    FROM\n        viewConfigRecord"
+ "    SELECT\n        name, configHash\n    FROM\n        viewConfigRecord"
+ "    SELECT\n        s.sourceType,\n        slc.configIndex,\n        s.updateType,\n        s.sourceIdentifier,\n        sls.sourceListenerId\n    FROM\n        sourceListenerState sls\n    JOIN\n        sourceState s\n    ON\n        s.sourceId = sls.sourceId\n    JOIN\n        sourceListenerConfig slc\n    ON\n        slc.sourceListenerConfigId = sls.sourceListenerConfigId\n    WHERE\n        slc.viewOrderedId = ?"
+ "    SELECT\n        s.sourceType,\n        slc.configIndex,\n        s.updateType,\n        s.sourceIdentifier,\n        sls.sourceListenerId\n    FROM\n        sourceListenerStateFullRebuild sls\n    JOIN\n        sourceState s\n    ON\n        s.sourceId = sls.sourceId\n    JOIN\n        sourceListenerConfig slc\n    ON\n        slc.sourceListenerConfigId = sls.sourceListenerConfigId\n    WHERE\n        slc.viewOrderedId = ?"
+ "    SELECT\n        slc.schedule\n    FROM\n        sourceListenerConfig slc\n    JOIN\n        sourceListenerState sls\n    ON\n        slc.sourceListenerConfigId = sls.sourceListenerConfigId\n    WHERE\n        sls.sourceListenerId = ?"
+ "    SELECT\n        slc.schedule,\n        slc.requiredSource,\n        slc.computeIfPastSLA,\n        slc.highPriority,\n        slc.viewOrderedId\n    FROM\n        sourceListenerState sls\n    JOIN\n        sourceListenerConfig slc\n    ON\n        sls.sourceListenerConfigId = slc.sourceListenerConfigId\n    WHERE\n        sls.sourceListenerId = ?"
+ "    SELECT\n        sls.sourceListenerId,\n        sls.sourceId\n    FROM\n        sourceListenerState sls\n    JOIN\n        sourceListenerConfig slc\n    ON\n        sls.sourceListenerConfigId = slc.sourceListenerConfigId\n    WHERE\n        slc.viewOrderedId = ?"
+ "    SELECT\n        sls.sourceListenerId,\n        sls.sourceId,\n        s.available\n    FROM\n        sourceListenerState sls\n    JOIN\n        sourceListenerConfig slc\n    ON\n        sls.sourceListenerConfigId = slc.sourceListenerConfigId\n    JOIN\n        sourceState s\n    ON\n        s.sourceId = sls.sourceId\n    WHERE\n        slc.viewOrderedId = ?"
+ "    SELECT\n        sls.sourceListenerId,\n        sls.sourceId,\n        slc.computeIfPastSLA,\n        slc.schedule\n    FROM\n        sourceListenerState sls\n    JOIN\n        sourceListenerConfig slc\n    ON\n        sls.sourceListenerConfigId = slc.sourceListenerConfigId\n    WHERE\n        slc.viewOrderedId = ?"
+ "    SELECT\n        sourceId\n    FROM\n        sourceState\n    WHERE\n        sourceType = "
+ "    SELECT\n        sourceId,\n        available\n    FROM\n        sourceState\n    WHERE\n        sourceType = ?\n    AND\n        sourceIdentifier = ?\n    AND\n        updateType = ?"
+ "    SELECT\n        sourceListenerId\n    FROM\n        sourceListenerState\n    WHERE\n        sourceListenerConfigId = ?"
+ "    SELECT\n        sourceListenerId\n    FROM\n        sourceListenerStateFullRebuild\n    WHERE\n        sourceListenerConfigId = ?"
+ "    SELECT\n        startView\n    FROM\n        scheduleState\n    WHERE\n        schedule = ?"
+ "    SELECT\n        updateGroup,\n        writeToStream\n    FROM\n        viewConfigRecord\n    WHERE\n        id = ?"
+ "    SELECT\n        vcr.name\n    FROM\n        viewConfigRecord vcr\n    JOIN\n        viewState vs\n    ON\n        vcr.id = vs.viewOrderedId\n    WHERE\n        vs.enabledStatus != "
+ "    SELECT\n        vcr.name\n    FROM\n        viewConfigRecord vcr\n    JOIN\n        viewState vs\n    WHERE\n        vcr.id = ?\n    AND\n        vs.viewOrderedId = vcr.id\n    AND\n        vs.enabledStatus = ?"
+ "    SELECT\n        viewOrderedId\n    FROM\n        updateQueue\n    WHERE\n        schedule = ?\n    AND\n        viewOrderedId = ?"
+ "    SELECT\n        viewOrderedId\n    FROM\n        updateQueue\n    WHERE\n        schedule = ?\n    AND\n        viewOrderedId >= ?"
+ "    SELECT DISTINCT\n        schedule\n    FROM\n        updateQueue"
+ "    SELECT DISTINCT\n        slc.viewOrderedId\n    FROM\n        sourceListenerConfig slc\n    JOIN\n        sourceListenerState sls\n    ON\n        slc.sourceListenerConfigId = sls.sourceListenerConfigId\n    WHERE\n        sls.sourceId = ?\n    AND\n        slc.requiredSource"
+ "    SELECT DISTINCT\n        value\n    FROM\n        viewConfigRecord records, json_each(records.viewUpdateDependencies)\n    WHERE\n        records.id = ?\n    ORDER BY\n        value ASC"
+ "    SELECT DISTINCT\n        value\n    FROM\n        viewConfigRecord records, json_each(records.viewUpdateDependents)\n    WHERE\n        records.id = ?\n    ORDER BY\n        value ASC"
+ "    SELECT DISTINCT\n        vcr.id,\n        vcr.name\n    FROM\n        viewConfigRecord vcr\n    JOIN\n        sourceListenerConfig slc\n    ON\n        vcr.id = slc.viewOrderedId\n    WHERE\n        slc.schedule = ?\n    ORDER BY\n        vcr.id"
+ "    UPDATE\n        scheduleState\n    SET\n        startView = ?\n    WHERE\n        \"schedule\" = ?"
+ "    UPDATE\n        sourceListenerState\n    SET\n        bookmark = ?\n    WHERE\n        sourceListenerId = ?"
+ "    UPDATE\n        sourceListenerState\n    SET\n        sourceUpdatedTimestamp = 0.0,\n        runByTimestamp = 0.0,\n        bookmark = NULL\n    FROM\n        sourceListenerConfig slc\n    WHERE\n        slc.viewOrderedId = ?\n    AND\n        sourceListenerState.sourceListenerConfigId = slc.sourceListenerConfigId"
+ "    UPDATE\n        sourceListenerState\n    SET\n        sourceUpdatedTimestamp = ?,\n        runByTimestamp = ?,\n        bookmark = ?\n    WHERE\n        sourceListenerId = ?"
+ "    UPDATE\n        sourceListenerState\n    SET\n        sourceUpdatedTimestamp = r_sls.sourceUpdatedTimestamp,\n        runByTimestamp = r_sls.runByTimestamp,\n        bookmark = r_sls.bookmark\n    FROM\n        rebuilding_sourceListenerState r_sls,\n        rebuilding_sourceListenerConfig r_slc,\n        rebuilding_viewConfigRecord r_vcr,\n        rebuilding_sourceState r_s,\n        sourceListenerConfig slc,\n        viewConfigRecord vcr,\n        sourceState s\n    WHERE\n    -- Join rebuilding tables, source - sourceListener - sourceListnerConfig - viewConfigRecord\n        r_s.sourceId = r_sls.sourceId\n    AND\n        r_sls.sourceListenerConfigId = r_slc.sourceListenerConfigId\n    AND\n        r_slc.viewOrderedId = r_vcr.id\n    AND\n    -- Join normal tables, source - sourceListener - sourceListnerConfig - viewConfigRecord\n        s.sourceId = sourceListenerState.sourceId\n    AND\n        sourceListenerState.sourceListenerConfigId = slc.sourceListenerConfigId\n    AND\n        slc.viewOrderedId = vcr.id\n    AND\n    -- Match all of the config items between old and new\n        vcr.name = r_vcr.name\n    AND\n        slc.sourceType = r_slc.sourceType\n    AND\n        slc.configIndex = r_slc.configIndex\n    AND\n        s.sourceType = r_s.sourceType\n    AND\n        s.sourceIdentifier = r_s.sourceIdentifier\n    AND\n        s.updateType = r_s.updateType"
+ "    UPDATE\n        sourceListenerStateFullRebuild\n    SET\n        bookmark = ?\n    WHERE\n        sourceListenerId = ?"
+ "    UPDATE\n        sourceListenerStateFullRebuild\n    SET\n        sourceUpdatedTimestamp = r_sls.sourceUpdatedTimestamp,\n        runByTimestamp = r_sls.runByTimestamp,\n        bookmark = r_sls.bookmark\n    FROM\n        rebuilding_sourceListenerStateFullRebuild r_sls,\n        rebuilding_sourceListenerConfig r_slc,\n        rebuilding_viewConfigRecord r_vcr,\n        rebuilding_sourceState r_s,\n        sourceListenerConfig slc,\n        viewConfigRecord vcr,\n        sourceState s\n    WHERE\n    -- Join rebuilding tables, source - sourceListener - sourceListnerConfig - viewConfigRecord\n        r_s.sourceId = r_sls.sourceId\n    AND\n        r_sls.sourceListenerConfigId = r_slc.sourceListenerConfigId\n    AND\n        r_slc.viewOrderedId = r_vcr.id\n    AND\n    -- Join normal tables, source - sourceListener - sourceListnerConfig - viewConfigRecord\n        s.sourceId = sourceListenerStateFullRebuild.sourceId\n    AND\n        sourceListenerStateFullRebuild.sourceListenerConfigId = slc.sourceListenerConfigId\n    AND\n        slc.viewOrderedId = vcr.id\n    AND\n    -- Match all of the config items between old and new\n        vcr.name = r_vcr.name\n    AND\n        slc.sourceType = r_slc.sourceType\n    AND\n        slc.configIndex = r_slc.configIndex\n    AND\n        s.sourceType = r_s.sourceType\n    AND\n        s.sourceIdentifier = r_s.sourceIdentifier\n    AND\n        s.updateType = r_s.updateType"
+ "    UPDATE\n        sourceState\n    SET\n        available = 0\n    WHERE\n        sourceId = ?\n    AND\n        available != 0"
+ "    UPDATE\n        sourceState\n    SET\n        modifiedTimestamp = ?,\n        available = ?\n    WHERE\n        sourceId = ?"
+ "    UPDATE\n        sourceState\n    SET\n        modifiedTimestamp = rs.modifiedTimestamp,\n        available = rs.available\n    FROM\n        rebuilding_sourceState rs\n    WHERE\n        sourceState.sourceType = rs.sourceType\n    AND\n        sourceState.sourceIdentifier = rs.sourceIdentifier\n    AND\n        sourceState.updateType = rs.updateType"
+ "    UPDATE\n        viewState\n    SET\n        attemptCount = ?\n    WHERE\n       viewOrderedId = ?"
+ "    UPDATE\n        viewState\n    SET\n        attemptCount = attemptCount + 1\n    WHERE\n       viewOrderedId = ?"
+ "    UPDATE\n        viewState\n    SET\n        bookmark = ?\n    WHERE\n       viewOrderedId = ?"
+ "    UPDATE\n        viewState\n    SET\n        bookmark = rvs.bookmark,\n        tablesCreated = rvs.tablesCreated\n    FROM\n        rebuilding_viewState rvs,\n        viewConfigRecord vcr,\n        rebuilding_viewConfigRecord rvcr\n    WHERE\n        rvs.viewOrderedId = rvcr.id\n    AND\n        viewState.viewOrderedId = vcr.id\n    AND\n        rvcr.name = vcr.name\n    AND\n        viewState.diffType = rvs.diffType"
+ "    UPDATE\n        viewState\n    SET\n        enabledStatus = ?,\n        attemptCount = ?,\n        errorMessage = ?,\n        bookmark = ?\n    WHERE\n        viewOrderedId = ?"
+ "    UPDATE\n        viewState\n    SET\n        enabledStatus = ?,\n        errorMessage = ?\n    WHERE\n       viewOrderedId = ?"
+ "    UPDATE\n        viewState\n    SET\n        tablesCreated = ?\n    WHERE\n       viewOrderedId = ?"
+ " - view may be running 🏃"
+ " does not existing in the view configuration "
+ " found in sla queue unexpectedly"
+ " is not monitoring changes"
+ " is not monitoring computeIfPastSLA state"
+ " is unexpectedly monitoring changes"
+ "$__lazy_storage_$_photoLibrary"
+ ",\n        0,\n        "
+ ",\n        0,\n        '',\n        "
+ ",\n        0.0,\n        0.0,\n        NULL\n    )"
+ ",\n        NULL\n    )"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/GRDB/GRDB/Core/Row.swift"
+ "<ViewState id: '"
+ "Attempting to fully rebuild view using incremental bookmarks"
+ "Attempting to process a view too many times. Likely crashed during a view update"
+ "Cannot encode json array"
+ "DELETE FROM computeIfPastSLA"
+ "DELETE FROM debounceSourceAction"
+ "DELETE FROM updateQueue"
+ "Disabled via iptool"
+ "Expected at least one request"
+ "Incorrect verbose level "
+ "Invalid bookmark width "
+ "Mismatch in requests and configuration"
+ "Missing deletion for update request "
+ "Missing request for update request "
+ "No device for deviceId "
+ "No id for response configIdentifer "
+ "No request for response for "
+ "No schedule for sourceListenerId "
+ "No source listener state for sourceListenerId "
+ "No source state for sourceId "
+ "No view found for name"
+ "No view state for view id "
+ "Unexpected: Attempting to remove a view that doesn't exist"
+ "Unexpected: no view for path"
+ "Unexpectedly retrieving control source"
+ "_TtCC24IntelligencePlatformCore12ViewDatabase13OutputBuilder"
+ "_TtCC24IntelligencePlatformCore12ViewDatabase14StatementCache"
+ "_TtCC24IntelligencePlatformCore12ViewDatabaseP33_3FB48FF3C0456F9C62EDE60203FA35C230SourceListenerValidationResult"
+ "_TtCCO24IntelligencePlatformCore10ViewUpdate15FrontEventQueue13CoalesceState"
+ "_TtCCO24IntelligencePlatformCore10ViewUpdate7Manager20SourceResourceHolder"
+ "_TtCO24IntelligencePlatformCore10ViewUpdate15FrontEventQueue"
+ "_TtCO24IntelligencePlatformCore10ViewUpdate18BiomeRequestSource"
+ "_TtCO24IntelligencePlatformCore10ViewUpdate21KeyValueRequestSource"
+ "_TtCO24IntelligencePlatformCore10ViewUpdate27KnowledgeGraphRequestSource"
+ "_TtCO24IntelligencePlatformCore10ViewUpdate33GlobalKnowledgeGraphRequestSource"
+ "autonamingMessagesPhotosProcessingProgress"
+ "biomeListeners"
+ "changesRequested"
+ "computeIfPastSLA_timeIdx"
+ "currentDeleteBlob"
+ "debounceSourceAction"
+ "debounceState"
+ "devices"
+ "disabled [too many update attempts]"
+ "errors"
+ "expectedInAQueue"
+ "expectedInLiveQueue"
+ "expectedInQueue"
+ "expectedInSLA"
+ "expectedMonitoring"
+ "first"
+ "frontQueue"
+ "fullRebuild.db-shm"
+ "fullReubild.db-wal"
+ "globalKnowledgeStoreBacking"
+ "graphStoreBacking"
+ "has not updated and is unavailable"
+ "has sourceState set to available when the view is unavailable"
+ "has sourceState set to unavailable when the view is available"
+ "has unavailable required source and cannot update: "
+ "hasAllRequiredSources"
+ "hasDeletes"
+ "initialDeleteBlob"
+ "is not queued in "
+ "is not queued in any queue - "
+ "is not queued in the live queue, which is expected by - "
+ "isInAQueue"
+ "isInLiveQueue"
+ "isInQueue"
+ "isInSLA"
+ "isMonitored"
+ "keyValueStoreBacking"
+ "keyValueStoreGenerator"
+ "lastBuildGraphFromScratchTimestamp"
+ "latestDeleteBlob"
+ "no sourceListenerState for id"
+ "no viewConfigRecord for id"
+ "result"
+ "retryFailures"
+ "scheduleForSlid"
+ "scheduleState"
+ "simpleInfo"
+ "slaState"
+ "sourceListener"
+ "sourceListenerConfig"
+ "sourceListenerConfigId"
+ "sourceListenerConfig_config"
+ "sourceListenerConfig_idx"
+ "sourceListenerConfig_scheduleIdx"
+ "sourceListenerId"
+ "sourceListenerStateFullRebuild"
+ "sourceListenerStateFullRebuild_slcid_idx"
+ "sourceListenerStateFullRebuild_src_idx"
+ "sourceListenerState_slcid_idx"
+ "sourceListenerState_src_idx"
+ "sourceListener_bookmark"
+ "sourceResourceHolder"
+ "sourceState"
+ "sourcesMonitored"
+ "statementCacheBacking"
+ "tables are not created"
+ "triggeredViews"
+ "updateGroupAndWriteToStream"
+ "updateQueue"
+ "updateType"
+ "v44@0:8@\"GDViewQuery\"16B24q28@?<v@?@\"NSString\"@\"NSError\">36"
+ "viewHasUnavailableRequiredSource"
+ "viewIdsWithRequiredSource"
+ "viewNameIfEnabled"
+ "viewSourceStateModifiedTimestamp"
+ "viewState"
+ "viewState_bookmark"
+ "viewWasClearedInfo"
+ "viewWasDisabled"
+ "viewWillUpdate"
+ "views must be listed as a dependency if used in the update SQL ("
+ "viewsForSchedule"
+ "{\"deletionTimestamp\": "
+ "🔴 blocked by unavailable sources "
+ "🟠 unavailable (no pending updates)"
+ "🟠 unavailable - queued on "
+ "🟢 available ("
- "\n            AND sourceIdentifier = "
- "\n            AND updateType = "
- "\n        WHERE\n            sourceType = "
- "\n    AND\n        alwaysAvailable = "
- "\n    AND\n        diffType = "
- "\n    AND\n        forFullRebuild = "
- "\n    ORDER BY\n        value ASC"
- "\n    WHERE\n        schedule = "
- "\n    WHERE\n       name = "
- "        UPDATE\n            sourceTimestamps\n        SET\n            timestamp = "
- "        WITH sourceListenerStateSourceKeys\n        AS (\n            SELECT DISTINCT\n                sourceType, sourceIdentifier\n            FROM\n                sourceListenerState\n        )\n\n        DELETE FROM\n            sourceTimestamps\n        WHERE\n            (sourceType, sourceIdentifier) NOT IN sourceListenerStateSourceKeys"
- "    DELETE FROM\n        sourceListenerState\n    WHERE\n        view\n    NOT IN (\n        SELECT\n            name\n        FROM\n            viewConfigRecord\n    )"
- "    DELETE FROM\n        sourceState\n    WHERE\n        (type, identifier)\n    NOT IN (\n        SELECT DISTINCT\n            sourceType,\n            sourceIdentifier\n        FROM\n            sourceListenerState\n    )"
- "    DELETE FROM\n        sourceState\n    WHERE\n        type = ? AND identifier = ?"
- "    DELETE FROM\n        view_schedule\n    WHERE\n        schedule = ?"
- "    DELETE FROM\n        view_state\n    WHERE\n        name = "
- "    DELETE FROM\n        view_state\n    WHERE\n        name = ?"
- "    DELETE FROM\n        view_state\n    WHERE\n        view_state.name\n    NOT IN (\n        SELECT\n            name\n        FROM\n            viewConfigRecord\n    )"
- "    DELETE FROM viewConfigRecord WHERE name = 'Dummy'"
- "    INSERT INTO viewConfigRecord(\"name\", \"configHash\") VALUES ('Dummy', '0');"
- "    INSERT INTO viewConfigRecord(\"name\", \"configHash\") VALUES ('Dummy', '1');"
- "    SELECT\n        *\n    FROM\n        sourceState\n    WHERE\n        type = ?"
- "    SELECT\n        *\n    FROM\n        view_state\n    WHERE\n        name = "
- "    SELECT\n        1\n    FROM\n        view_state\n    WHERE\n        name = "
- "    SELECT\n        name\n    FROM\n        view_state\n    WHERE\n        enabledStatus != "
- "    SELECT\n        startView\n    FROM\n        view_schedule\n    WHERE\n        schedule = "
- "    SELECT\n        vr.id AS orderedId,\n        vr.updateGroup AS updateGroup,\n        vr.writeToStream AS writeToStream,\n        vs.alwaysAvailable AS alwaysAvailable,\n        vs.diffType AS diffType,\n        vs.bookmark AS bookmark,\n        vs.name AS name,\n        vs.enabledStatus AS enabledStatus,\n        vs.attemptCount AS attemptCount\n    FROM\n        view_state vs\n    JOIN\n        viewConfigRecord vr\n    ON\n        vs.name = vr.name"
- "    SELECT\n       id\n    FROM\n       viewConfigRecord\n    WHERE\n       name = ?"
- "    SELECT\n       name\n    FROM\n       viewConfigRecord\n    ORDER BY\n       id"
- "    SELECT DISTINCT\n        value\n    FROM\n        viewConfigRecord records, json_each(records.viewUpdateDependencies)\n    WHERE\n        records.id = "
- "    SELECT DISTINCT\n        value\n    FROM\n        viewConfigRecord records, json_each(records.viewUpdateDependents)\n    WHERE\n        records.id = "
- "    SELECT count(*) FROM viewConfigRecord;"
- "    UPDATE\n        sourceListenerState\n    SET\n        bookmark = NULL\n    WHERE\n        view = "
- "    UPDATE\n        sourceListenerState\n    SET\n        sourceUpdatedTimestamp = 0,\n        runByTimestamp = 0,\n        bookmark = NULL"
- "    UPDATE\n        sourceListenerState\n    SET\n        sourceUpdatedTimestamp = 0,\n        runByTimestamp = 0,\n        bookmark = NULL\n    WHERE\n        sourceType = ? AND sourceIdentifier = ?"
- "    UPDATE\n        sourceState\n    SET\n        modifiedTimestamp = 0,\n        available = 0\n    WHERE\n        type = "
- "    UPDATE\n        view_schedule\n    SET\n        startView = "
- "    UPDATE\n        view_state\n    SET"
- "    UPDATE\n        view_state\n    SET\n        attemptCount = "
- "    UPDATE\n        view_state\n    SET\n        attemptCount = 0,\n        enabledStatus = "
- "    UPDATE\n        view_state\n    SET\n        attemptCount = attemptCount + 1\n    WHERE\n        name = "
- "    UPDATE\n        view_state\n    SET\n        enabled = "
- "    UPDATE\n        view_state\n    SET\n        enabledStatus = "
- "   WHERE\n      name = "
- " WHERE view = ? AND sourceType = ? AND configIndex = ? AND forFullRebuild = ?"
- " alwaysAvailable: "
- " attemptCount = "
- " enabledStatus = "
- " errorMessage = "
- " for source type "
- " or final bookmark ("
- " source should not have availability"
- "' enabledStatus: "
- ",\n        attemptCount = 0,\n        bookmark = NULL,\n        errorMessage = NULL\n    WHERE\n       name = "
- ",\n        bookmark = NULL"
- ",\n        errorMessage = "
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/GRDB/GRDB/Core/Row.swift"
- "<SourceTimestamp s:"
- "<ViewCleanup name: '"
- "<ViewState name: '"
- "Config data is not a string"
- "DELETE FROM\n    sourceListenerState\nWHERE\n    view = ?"
- "DELETE FROM sourceListenerState WHERE sourceType = 'biome'"
- "DELETE FROM sourceListenerState WHERE sourceType = 'knowledgeGraph'"
- "DELETE FROM view_config_hash"
- "DELETE FROM view_state"
- "DROP TABLE IF EXISTS grdb_migrations"
- "DROP TABLE view_bookmark"
- "DROP TABLE view_config_hash"
- "INSERT INTO\n    sourceListenerState_new (\n        view,\n        sourceType,\n        configIndex,\n        sourceIdentifier,\n        sourceUpdatedTimestamp,\n        schedule,\n        runByTimestamp,\n        bookmark,\n        computeIfPastSLA,\n        requiredSource,\n        highPriority,\n        rebuildView,\n        fullRebuildOnChange,\n        forFullRebuild,\n        config\n    )\nSELECT\n        view,\n        sourceType,\n        configIndex,\n        sourceIdentifier,\n        sourceUpdatedTimestamp,\n        schedule,\n        runByTimestamp,\n        bookmark,\n        computeIfPastSLA,\n        requiredSource,\n        highPriority,\n        0,\n        0,\n        0,\n        config\nFROM\n    sourceListenerState"
- "INSERT INTO sourceTimestamps (sourceType, sourceIdentifier, updateType, timestamp)\nSELECT 'biome', stream, 'deletion', deletionTimestamp\nFROM biomeDeletion"
- "Invalid config identifier schedule: "
- "Invalid source type for view "
- "No response for request for "
- "No sourceListenerState for config identifier "
- "SELECT\n    *\nFROM\n    sourceListenerState\nWHERE\n    view = ? AND forFullRebuild = ?"
- "SELECT 1 FROM grdb_migrations WHERE identifier = :name"
- "SELECT schedule FROM view_schedule"
- "STDatestampClientSessionIDClientRequestIDIndexView"
- "UPDATE sourceListenerState SET "
- "UPDATE sourceListenerState SET computeIfPastSLA = NULL"
- "UPDATE sourceListenerState SET config = NULL"
- "Unable to decode current bookmark ("
- "Unable to find full rebuild source listener for "
- "Unable to get view state for view id "
- "Unexpectedly decoding a control source"
- "Unsupported update type "
- "_TtCCO24IntelligencePlatformCore10ViewUpdate13SourceUpdater13CoalesceState"
- "_TtCCO24IntelligencePlatformCore10ViewUpdate13ViewUpdateJob13LiveViewQueue"
- "_TtCO24IntelligencePlatformCore10ViewUpdate11SourceState"
- "_TtCO24IntelligencePlatformCore10ViewUpdate13ScheduleState"
- "_TtCO24IntelligencePlatformCore10ViewUpdate14SourceListener"
- "_TtCO24IntelligencePlatformCore10ViewUpdate17ViewPriorityQueue"
- "_TtCO24IntelligencePlatformCore10ViewUpdate20ViewNextRunTimeQueue"
- "_TtCO24IntelligencePlatformCore10ViewUpdate28KnowledgeGraphSourceProvider"
- "_TtCO24IntelligencePlatformCore10ViewUpdate34GlobalKnowledgeGraphSourceProvider"
- "_TtCO24IntelligencePlatformCore10ViewUpdate9ViewState"
- "atomicFullRebuild"
- "attemptCount"
- "available"
- "cannot find view state"
- "computeIfPastSLAForAllListeners"
- "convertBiomeDeletionToSourceTimestamps"
- "convertEnabledStatusToEnum"
- "createConfigRecord"
- "deletionTimestamp"
- "disabled [crashed process during view update]"
- "disabled by tooling"
- "dropDependenciesField"
- "enabled"
- "ensureComputeIfPastSLAMigration"
- "ensurePerformMigration"
- "errorMessage"
- "fullRebuildSourceListeners"
- "globalKnowledgeGraphSourceProvider"
- "group"
- "highPriority"
- "inQueue"
- "keyValueSourceProvider"
- "knowledgeGraphSourceProvider"
- "launched"
- "nextRunTimeQueue"
- "order"
- "performUpdateInner"
- "persistErrorMessage"
- "persist_attempt_count"
- "priorityQueue"
- "rebuildView"
- "rebuildViews"
- "removeAllowedClients"
- "rename_sourceIdentifier"
- "requiredSource"
- "requiredSourceDefaultTrue"
- "resetAttemptCount"
- "runByTimestamp"
- "runByTimestamp = ?"
- "scheduleStartView"
- "scheduleToSource"
- "scheduledTimestamp"
- "schedules"
- "sourceKey"
- "sourceKeyToViewNames"
- "sourceListenerPriority"
- "sourceListenerState_new"
- "sourceListeners"
- "sourceStateStatus"
- "sourceTimestamp"
- "sourceTimestamps"
- "sourceUpdatedTimestamp = ?"
- "sourceUpdater"
- "triggerMigrationDueToFeatureChange"
- "updatedBiomeBookmarks"
- "updatedBiomeBookmarksAddFirstEventBookmark"
- "updatedBiomeBookmarksRemoveFirstEventBookmark"
- "updatedKnowledgeGraphBookmarks"
- "updatedKnowledgeGraphBookmarksAgain"
- "viewConfigRecord_name_config_idx"
- "viewDependencies"
- "viewKeyValueTable"
- "viewState not found"
- "view_config_hash"
- "views"
- "viewsByName"
- "writeToStream"

```
