## analyticsd

> `/System/Library/PrivateFrameworks/CoreAnalytics.framework/Support/analyticsd`

```diff

-419.60.7.0.0
-  __TEXT.__text: 0xeebc4
-  __TEXT.__auth_stubs: 0x1ac0
-  __TEXT.__objc_stubs: 0x18a0
+430.100.6.0.0
+  __TEXT.__text: 0xeb980
+  __TEXT.__auth_stubs: 0x1a00
+  __TEXT.__objc_stubs: 0x1920
   __TEXT.__init_offsets: 0x20
-  __TEXT.__objc_methlist: 0x264
+  __TEXT.__objc_methlist: 0x23c
   __TEXT.__cstring: 0xe7ae
-  __TEXT.__const: 0x989d
-  __TEXT.__gcc_except_tab: 0xdf68
-  __TEXT.__oslogstring: 0x13ea2
-  __TEXT.__objc_classname: 0x68
-  __TEXT.__objc_methtype: 0x44d
-  __TEXT.__objc_methname: 0x1295
-  __TEXT.__constg_swiftt: 0x94
-  __TEXT.__swift5_typeref: 0x71
-  __TEXT.__swift5_fieldmd: 0x38
-  __TEXT.__swift5_types: 0x8
-  __TEXT.__swift5_reflstr: 0x17
-  __TEXT.__unwind_info: 0x5f38
-  __DATA_CONST.__auth_got: 0xd78
-  __DATA_CONST.__got: 0x4a0
+  __TEXT.__const: 0x98d5
+  __TEXT.__gcc_except_tab: 0xe0c0
+  __TEXT.__oslogstring: 0x13f21
+  __TEXT.__objc_classname: 0x51
+  __TEXT.__objc_methtype: 0x3a0
+  __TEXT.__objc_methname: 0x1176
+  __TEXT.__constg_swiftt: 0x38
+  __TEXT.__swift5_typeref: 0x3f
+  __TEXT.__swift5_fieldmd: 0x10
+  __TEXT.__swift5_types: 0x4
+  __TEXT.__unwind_info: 0x5db0
+  __DATA_CONST.__auth_got: 0xd18
+  __DATA_CONST.__got: 0x4c8
   __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0x9428
-  __DATA_CONST.__cfstring: 0x8c0
-  __DATA_CONST.__objc_classlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x20
+  __DATA_CONST.__const: 0x9410
+  __DATA_CONST.__cfstring: 0x9e0
+  __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA.__objc_const: 0x850
-  __DATA.__objc_selrefs: 0x680
+  __DATA.__objc_const: 0x4d0
+  __DATA.__objc_selrefs: 0x698
   __DATA.__objc_ivar: 0x40
-  __DATA.__objc_data: 0x2d8
-  __DATA.__data: 0x508
-  __DATA.__bss: 0x480
-  __DATA.__common: 0x18
+  __DATA.__objc_data: 0x1f0
+  __DATA.__data: 0x420
+  __DATA.__bss: 0x488
+  __DATA.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/Versions/A/CoreLocation
   - /System/Library/Frameworks/CoreMotion.framework/Versions/A/CoreMotion

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 8B933EAE-6713-3CDF-AD2C-7DE3B4169CA0
-  Functions: 4700
-  Symbols:   617
-  CStrings:  2779
+  UUID: 058346FC-545D-33F3-9A0E-5E2D20D49BA1
+  Functions: 4638
+  Symbols:   610
+  CStrings:  2756
 
Symbols:
+ _$sSS10FoundationE19_bridgeToObjectiveCSo8NSStringCyF
+ _$sSS10FoundationEySSSo8NSStringCcfC
+ _$ss018_bridgeAnyObjectToB0yypyXlSgF
+ _$ss20__StaticArrayStorageCN
+ _OBJC_CLASS_$_BMSQLDatabase
+ _OBJC_CLASS_$_OSADefaults
+ _OBJC_CLASS_$_TRIExperimentIdentifiers
+ __ZNSt3__117bad_function_callD1Ev
+ __ZTINSt3__117bad_function_callE
+ __ZTVNSt3__117bad_function_callE
+ __swiftImmortalRefCount
+ _swift_dynamicCast
+ _swift_getObjCClassMetadata
+ _xpc_array_append_value
+ _xpc_array_create_empty
- _$s3XPC0A11_TYPE_ERRORs13OpaquePointerVvg
- _$s3XPC0A16_TYPE_DICTIONARYs13OpaquePointerVvg
- _$sSS10FoundationE36_unconditionallyBridgeFromObjectiveCySSSo8NSStringCSgFZ
- _$sSS10describingSSx_tclufC
- _$sSo13os_log_type_ta0A0E5debugABvgZ
- _$sSw10copyMemory4fromySW_tF
- _$sSwys5UInt8VSicis
- _$ss17_assertionFailure__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- _$ss18_fatalErrorMessage__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- _SCDynamicStoreCopyConsoleUser
- __Block_copy
- __Block_release
- __ZNKSt9exception4whatEv
- _geteuid
- _swift_arrayDestroy
- _swift_beginAccess
- _swift_deletedMethodError
- _swift_initStackObject
- _swift_isaMask
- _swift_unknownObjectRetain_n
- _xpc_connection_send_message_with_reply_sync
- _xpc_connection_set_target_uid
CStrings:
+ "Activation row: %@"
+ "Figuring out which experiments are still active"
+ "Get oldest activation for this namespace"
+ "GreyMatterAvailable"
+ "Number of deactivations: %ld for experimentId: %@"
+ "Oldest activation for this namespace: %@"
+ "Reading activation rows for Namespace: %@"
+ "Reading user id's with experiments in the Trial Biome Stream"
+ "SELECT * FROM \"Trial.Experiment.NamespaceUpdates\" WHERE userId = '%@' AND experimentStatus = 1 AND EXISTS ( SELECT 1 FROM json_each(json_extract(NamespaceNames_json, '$.namespaceName')) WHERE json_each.value = '%@' ) ORDER BY eventTimestamp DESC LIMIT 1"
+ "SELECT COUNT(*) as row_count FROM \"Trial.Experiment.NamespaceUpdates\" WHERE experimentId = '%@' AND deploymentId = '%@' AND treatmentId = '%@' AND userID = '%@' AND experimentStatus = 2 AND eventTimestamp > '%@'"
+ "SELECT DISTINCT userId FROM \"Trial.Experiment.NamespaceUpdates\""
+ "Unable to unwrap availability reasons array"
+ "Unable to unwrap availability string"
+ "Unexpected object for key: %s"
+ "[TrialStateRelay] TrialIdentifier from Biome: experimentIdentifiers for namespace %@ are: experimentId: %@, deploymentId: %d, treatmentId: %@"
+ "_refreshTrialStateFromBiome:"
+ "app-usage-sync"
+ "config-dump"
+ "config-reload"
+ "eventTimestamp"
+ "executeQuery:"
+ "initWithExperimentId:deploymentId:treatmentId:"
+ "insert-query-state"
+ "last"
+ "list-transforms-in-cache"
+ "longValue"
+ "next"
+ "overrideBasebandFirmwareVersionString"
+ "query-clear"
+ "reasons"
+ "row"
+ "row_count"
+ "set-clear-config-after-reboot"
+ "store-locale-info"
+ "userId"
+ "userId: %@ with experiment event"
+ "{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}8@?0"
+ "{optional<std::string>=(?=c{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}})B}16@0:8"
+ "{pair<std::string, double>={basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}d}8@?0"
- "#16@0:8"
- "@\"NSString\"16@0:8"
- "@24@0:8:16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "Failed to subscribe to user data changes"
- "Fatal error"
- "Got unexpected response from analyticsagent"
- "Insufficient space allocated to copy string contents"
- "NSObject"
- "OS_xpc_object"
- "Q16@0:8"
- "Received an XPC error reply: %s"
- "Setting target user uid to %u"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "There are no logged in users yet..."
- "Unexpected XPC: %{public}s"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "Vv16@0:8"
- "XPC error: %{public}s"
- "YES"
- "[TrialStateRelay] TrialIdentifier: experimentIdentifiers for namespace %@ are: experimentId: %@, deploymentId: %d, treatmentId: %@"
- "[TrialStateRelay] TrialIdentifier: experimentIdentifiers nil. No active experiment"
- "^{_NSZone=}16@0:8"
- "_TtC10analyticsd23AnalyticsXPCQueryClient"
- "_connection"
- "analytics_user_data"
- "autorelease"
- "class"
- "com.apple.analyticsagent"
- "conformsToProtocol:"
- "debugDescription"
- "experimentIdentifiersWithNamespaceName:"
- "hash"
- "invalid Collection: less than 'count' elements in collection"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "keyMapping"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "refresh"
- "release"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "subscribeToUserDataChangesWithArguments:"
- "superclass"
- "v16@?0@\"<OS_xpc_object>\"8"
- "zone"
- "{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}8@?0"
- "{optional<std::string>=(?=c{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}})B}16@0:8"
- "{pair<std::string, double>={basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}d}8@?0"

```
