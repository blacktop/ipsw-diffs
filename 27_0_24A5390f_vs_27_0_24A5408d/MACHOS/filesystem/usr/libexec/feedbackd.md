## feedbackd

> `/usr/libexec/feedbackd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_entry`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-232.0.0.0.0
-  __TEXT.__text: 0x77854
-  __TEXT.__auth_stubs: 0x1ed0
+235.0.0.0.0
+  __TEXT.__text: 0x78a0c
+  __TEXT.__auth_stubs: 0x1f80
   __TEXT.__objc_stubs: 0x1340
   __TEXT.__objc_methlist: 0x558
-  __TEXT.__const: 0x1dd8
-  __TEXT.__swift5_typeref: 0xd10
-  __TEXT.__oslogstring: 0x278f
-  __TEXT.__cstring: 0x2c45
+  __TEXT.__const: 0x1e08
+  __TEXT.__swift5_typeref: 0xd44
+  __TEXT.__oslogstring: 0x279f
+  __TEXT.__cstring: 0x2c85
   __TEXT.__constg_swiftt: 0xbec
   __TEXT.__swift5_fieldmd: 0x780
   __TEXT.__swift5_builtin: 0x64

   __TEXT.__objc_classname: 0x46c
   __TEXT.__objc_methname: 0x192d
   __TEXT.__objc_methtype: 0x852
-  __TEXT.__swift5_capture: 0x724
+  __TEXT.__swift5_capture: 0x734
   __TEXT.__swift_as_entry: 0x108
   __TEXT.__swift_as_cont: 0x450
   __TEXT.__swift_as_ret: 0x140
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x15b0
-  __TEXT.__eh_frame: 0x43f0
-  __DATA_CONST.__const: 0x1de0
+  __TEXT.__unwind_info: 0x15e8
+  __TEXT.__eh_frame: 0x4478
+  __DATA_CONST.__const: 0x1e08
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x60
-  __DATA_CONST.__auth_got: 0xf70
-  __DATA_CONST.__got: 0x7b0
-  __DATA_CONST.__auth_ptr: 0x3f0
+  __DATA_CONST.__auth_got: 0xfc8
+  __DATA_CONST.__got: 0x7d0
+  __DATA_CONST.__auth_ptr: 0x3f8
   __DATA.__objc_const: 0x1c28
   __DATA.__objc_selrefs: 0x670
   __DATA.__objc_data: 0x880

   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/FeedbackService.framework/FeedbackService
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
+  - /System/Library/PrivateFrameworks/IntelligencePlatformQuery.framework/IntelligencePlatformQuery
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1436
-  Symbols:   854
-  CStrings:  749
+  Functions: 1451
+  Symbols:   870
+  CStrings:  755
 
Symbols:
+ _$s25IntelligencePlatformQuery12ResultColumnV12currentValueSSSgyF
+ _$s25IntelligencePlatformQuery12ResultColumnV12currentValueSiyF
+ _$s25IntelligencePlatformQuery12ResultColumnVMa
+ _$s25IntelligencePlatformQuery13SQLConnectionC7execute5query8bindings5blockySS_SayAC8Bindable_pSgGyAA15ResultSetCursorCKXEtKF
+ _$s25IntelligencePlatformQuery13SQLConnectionC7useCase7accountACSo05BMUseF10Identifiera_So9BMAccountCSgtKcfC
+ _$s25IntelligencePlatformQuery13SQLConnectionC8BindableMp
+ _$s25IntelligencePlatformQuery13SQLConnectionCMa
+ _$s25IntelligencePlatformQuery15ResultSetCursorC3rowSDySSypSgGyKF
+ _$s25IntelligencePlatformQuery15ResultSetCursorC4stepSbyKF
+ _$s25IntelligencePlatformQuery15ResultSetCursorC6columnyAA0D6ColumnVSSKF
+ _$sSS25IntelligencePlatformQuery13SQLConnectionC8BindableAAWP
+ _$ss15_print_unlockedyyx_q_zts16TextOutputStreamR_r0_lF
+ _$ss26DefaultStringInterpolationVN
+ _$ss26DefaultStringInterpolationVs16TextOutputStreamsWP
+ _SBSRemoteAlertHandleInvalidationErrorDomain
+ _swift_retain_x8
CStrings:
+ "\n        )\n        AS rn FROM (\n            SELECT\n                json_extract(commonMetadata, '$.evaluationUuid') evaluationUuid,\n                replace(json_extract(commonMetadata, '$.evaluationUuid'), '-', '') compareableEvaluationUuid,\n                json_extract(commonMetadata, '$.featureDomain') featureDomain,\n                eventTimestamp,\n                commonMetadata\n            FROM (\n                SELECT\n                    eventTimestamp,\n                    commonMetadata\n                FROM \""
+ "\n    )\n    AS rn FROM (\n        SELECT\n            json_extract(commonMetadata, '$.evaluationUuid') evaluationUuid,\n            replace(json_extract(commonMetadata, '$.evaluationUuid'), '-', '') compareableEvaluationUuid,\n            json_extract(commonMetadata, '$.featureDomain') featureDomain,\n            eventTimestamp,\n            commonMetadata\n        FROM (\n            SELECT\n                eventTimestamp,\n                commonMetadata\n            FROM \""
+ "\n)\nSELECT\n    *\nFROM (\n    SELECT\n        *,\n        '"
+ " days')\n        AND evaluationUuid NOT IN (\n            "
+ "\"\n                UNION SELECT\n                    eventTimestamp,\n                    commonMetadata\n                FROM \""
+ "\"\n            UNION SELECT\n                eventTimestamp,\n                commonMetadata\n            FROM \""
+ "\"\n        )\n        WHERE datetime(eventTimestamp, 'unixepoch') >= datetime('now', '-"
+ "\"\n    WHERE evaluationUuid IN results\n    UNION SELECT\n        *,\n        '"
+ "\"\n)\nWHERE id = ?"
+ "$.dictionary._0."
+ "'\n        ) id\n    FROM \""
+ "' as stream,\n        json_extract(commonMetadata, '$.evaluationUuid') evaluationUuid,\n        generatedContent,\n        originalContent,\n        commonMetadata\n    FROM \""
+ "Duplicate values for key: '"
+ "Failed to execute IPSQL query: %@"
+ "Failed to initialize IPSQL connection: %@"
+ "FeedbackDonationFetch"
+ "FeedbackDuplicateCheck"
+ "Remote alert view service initialization failure: %{public}@"
+ "SELECT\n    count(*) count\nFROM (\n    SELECT\n        json_extract(\n            json_extract(\n                originalContent,\n                '$.text'\n            ),\n            '"
+ "SELECT\n    evaluationUuid\nFROM (\n    SELECT\n        featureDomain,\n        eventTimestamp,\n        evaluationUuid,\n        commonMetadata,\n        ROW_NUMBER()\n    OVER (\n        PARTITION BY json_extract(commonMetadata, '$.featureDomain')\n        ORDER BY eventTimestamp "
+ "Swift/NativeDictionary.swift"
+ "WITH results AS (\n    SELECT\n        evaluationUuid\n    FROM (\n        SELECT\n            featureDomain,\n            eventTimestamp,\n            evaluationUuid,\n            commonMetadata,\n            ROW_NUMBER()\n        OVER (\n            PARTITION BY json_extract(commonMetadata, '$.featureDomain')\n            ORDER BY eventTimestamp "
+ "fetchDonationIDs(count:fromLatest:excludingEvaluationIDs:connection:)"
+ "fetchDonations(count:fromLatest:excludingEvaluationIDs:connection:)"
- "\n        )\n        AS rn FROM (\n            SELECT\n                json_extract(commonMetadata_json, \"$.evaluationUuid\") evaluationUuid,\n                replace(json_extract(commonMetadata_json, \"$.evaluationUuid\"), \"-\", \"\") compareableEvaluationUuid,\n                json_extract(commonMetadata_json, \"$.featureDomain\") featureDomain,\n                eventTimestamp,\n                commonMetadata_json\n            FROM (\n                SELECT\n                    eventTimestamp,\n                    commonMetadata_json\n                FROM \""
- "\n    )\n    AS rn FROM (\n        SELECT\n            json_extract(commonMetadata_json, \"$.evaluationUuid\") evaluationUuid,\n            replace(json_extract(commonMetadata_json, \"$.evaluationUuid\"), \"-\", \"\") compareableEvaluationUuid,\n            json_extract(commonMetadata_json, \"$.featureDomain\") featureDomain,\n            eventTimestamp,\n            commonMetadata_json\n        FROM (\n            SELECT\n                eventTimestamp,\n                commonMetadata_json\n            FROM \""
- "\n)\nSELECT\n    *\nFROM (\n    SELECT\n        *,\n        \""
- " days\")\n        AND evaluationUuid NOT IN (\n            "
- "\"\n                UNION SELECT\n                    eventTimestamp,\n                    commonMetadata_json\n                FROM \""
- "\"\n            UNION SELECT\n                eventTimestamp,\n                commonMetadata_json\n            FROM \""
- "\"\n        )\n        WHERE datetime(eventTimestamp, \"unixepoch\") >= datetime(\"now\", \"-"
- "\"\n    WHERE evaluationUuid IN results\n    UNION SELECT\n        *,\n        \""
- "\" as stream,\n        json_extract(commonMetadata_json, \"$.evaluationUuid\") evaluationUuid,\n        generatedContent_json,\n        originalContent_json,\n        commonMetadata_json\n    FROM \""
- "%s - No error occurred"
- ".string._0\"\n        ) id\n    FROM \""
- "No duplicate row for spotlightID existed"
- "SELECT\n    count(*) count\nFROM (\n    SELECT\n        json_extract(\n            json_extract(\n                originalContent_json,\n                \"$.text\"\n            ),\n            \"$.dictionary._0."
- "SELECT\n    evaluationUuid\nFROM (\n    SELECT\n        featureDomain,\n        eventTimestamp,\n        evaluationUuid,\n        commonMetadata_json,\n        ROW_NUMBER()\n    OVER (\n        PARTITION BY json_extract(commonMetadata_json, \"$.featureDomain\")\n        ORDER BY eventTimestamp "
- "WITH results AS (\n    SELECT\n        evaluationUuid\n    FROM (\n        SELECT\n            featureDomain,\n            eventTimestamp,\n            evaluationUuid,\n            commonMetadata_json,\n            ROW_NUMBER()\n        OVER (\n            PARTITION BY json_extract(commonMetadata_json, \"$.featureDomain\")\n            ORDER BY eventTimestamp "
- "duplicate row count existed, but count didn't exist"
- "fetchDonationIDs(count:fromLatest:excludingEvaluationIDs:database:)"
- "fetchDonations(count:fromLatest:excludingEvaluationIDs:database:)"
```
