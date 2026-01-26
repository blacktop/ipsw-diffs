## HSTouchHIDService

> `/System/Library/HIDPlugins/ServicePlugins/HSTouchHIDService.plugin/HSTouchHIDService`

```diff

-9130.1.0.0.0
-  __TEXT.__text: 0xc640c
-  __TEXT.__auth_stubs: 0x1950
-  __TEXT.__objc_stubs: 0x61c0
-  __TEXT.__init_offsets: 0x1260
-  __TEXT.__objc_methlist: 0x49e8
-  __TEXT.__const: 0x3f1e
-  __TEXT.__gcc_except_tab: 0xd684
-  __TEXT.__cstring: 0xa180
-  __TEXT.__oslogstring: 0x3704
-  __TEXT.__objc_methname: 0x6e82
-  __TEXT.__objc_classname: 0xb7d
-  __TEXT.__objc_methtype: 0x54be
-  __TEXT.__unwind_info: 0x42a0
-  __DATA_CONST.__auth_got: 0xcb8
+9130.2.0.0.0
+  __TEXT.__text: 0xc7260
+  __TEXT.__auth_stubs: 0x1960
+  __TEXT.__objc_stubs: 0x6260
+  __TEXT.__init_offsets: 0x1280
+  __TEXT.__objc_methlist: 0x4a78
+  __TEXT.__const: 0x3f3e
+  __TEXT.__gcc_except_tab: 0xd788
+  __TEXT.__cstring: 0xa1d7
+  __TEXT.__oslogstring: 0x37c7
+  __TEXT.__objc_methname: 0x6f19
+  __TEXT.__objc_classname: 0xb9a
+  __TEXT.__objc_methtype: 0x59c5
+  __TEXT.__unwind_info: 0x4320
+  __DATA_CONST.__auth_got: 0xcc0
   __DATA_CONST.__got: 0x270
-  __DATA_CONST.__const: 0x1b40
-  __DATA_CONST.__cfstring: 0x6de0
-  __DATA_CONST.__objc_classlist: 0x380
+  __DATA_CONST.__const: 0x1b68
+  __DATA_CONST.__cfstring: 0x6e40
+  __DATA_CONST.__objc_classlist: 0x388
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x298
-  __DATA_CONST.__objc_intobj: 0x600
+  __DATA_CONST.__objc_superrefs: 0x2a0
+  __DATA_CONST.__objc_intobj: 0x618
   __DATA_CONST.__objc_doubleobj: 0xc0
   __DATA_CONST.__objc_arraydata: 0x518
   __DATA_CONST.__objc_arrayobj: 0x150
   __DATA_CONST.__objc_floatobj: 0x20
   __DATA_CONST.__objc_dictobj: 0x230
-  __DATA.__objc_const: 0x8920
-  __DATA.__objc_selrefs: 0x1d60
-  __DATA.__objc_ivar: 0x5bc
-  __DATA.__objc_data: 0x2300
+  __DATA.__objc_const: 0x8a38
+  __DATA.__objc_selrefs: 0x1d88
+  __DATA.__objc_ivar: 0x5cc
+  __DATA.__objc_data: 0x2350
   __DATA.__data: 0x1610
   __DATA.__bss: 0xc0
   __DATA.__common: 0x890

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5E0FA1F3-5BE5-37DC-AEC8-32B06E5E8811
-  Functions: 4692
-  Symbols:   26062
-  CStrings:  4490
+  UUID: CFC4C025-E007-3A8E-B573-9F8A36E52C98
+  Functions: 4715
+  Symbols:   26221
+  CStrings:  4512
 
Symbols:
+ -[HSTTelemetryAnalyticsStage .cxx_construct]
+ -[HSTTelemetryAnalyticsStage .cxx_destruct]
+ -[HSTTelemetryAnalyticsStage _handleFrame:]
+ -[HSTTelemetryAnalyticsStage _initializeReportIdMap]
+ -[HSTTelemetryAnalyticsStage _logPathReports]
+ -[HSTTelemetryAnalyticsStage _sendAnalyticsEvent:payload:]
+ -[HSTTelemetryAnalyticsStage _setupPeriodicTimer]
+ -[HSTTelemetryAnalyticsStage _trackReportID:]
+ -[HSTTelemetryAnalyticsStage dealloc]
+ -[HSTTelemetryAnalyticsStage handleConsume:]
+ -[HSTTelemetryAnalyticsStage initWithQueue:]
+ /Library/Caches/com.apple.xbs/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/HSTTelemetryAnalyticsStage.o
+ HSTTelemetryAnalyticsStage.mm
+ OBJC_IVAR_$_HSTTelemetryAnalyticsStage._periodicTimer
+ OBJC_IVAR_$_HSTTelemetryAnalyticsStage._queue
+ OBJC_IVAR_$_HSTTelemetryAnalyticsStage._receivedMask
+ OBJC_IVAR_$_HSTTelemetryAnalyticsStage._reportIdToBitMap
+ _AnalyticsSendEventLazy
+ _OBJC_CLASS_$_HSTTelemetryAnalyticsStage
+ _OBJC_METACLASS_$_HSTTelemetryAnalyticsStage
+ __Block_byref_object_copy_.421
+ __Block_byref_object_dispose_.422
+ __OBJC_$_INSTANCE_METHODS_HSTTelemetryAnalyticsStage
+ __OBJC_$_INSTANCE_VARIABLES_HSTTelemetryAnalyticsStage
+ __OBJC_CLASS_RO_$_HSTTelemetryAnalyticsStage
+ __OBJC_METACLASS_RO_$_HSTTelemetryAnalyticsStage
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIhhEENS_22__unordered_map_hasherIhS2_NS_4hashIhEENS_8equal_toIhEELb1EEENS_21__unordered_map_equalIhS2_S7_S5_Lb1EEENS_9allocatorIS2_EEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIhhEENS_22__unordered_map_hasherIhS2_NS_4hashIhEENS_8equal_toIhEELb1EEENS_21__unordered_map_equalIhS2_S7_S5_Lb1EEENS_9allocatorIS2_EEE25__emplace_unique_key_argsIhJRKNS_21piecewise_construct_tENS_5tupleIJRKhEEENSI_IJEEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS2_PvEEEEbEERKT_DpOT0_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIhhEENS_22__unordered_map_hasherIhS2_NS_4hashIhEENS_8equal_toIhEELb1EEENS_21__unordered_map_equalIhS2_S7_S5_Lb1EEENS_9allocatorIS2_EEE4findIhEENS_15__hash_iteratorIPNS_11__hash_nodeIS2_PvEEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIhhEENS_22__unordered_map_hasherIhS2_NS_4hashIhEENS_8equal_toIhEELb1EEENS_21__unordered_map_equalIhS2_S7_S5_Lb1EEENS_9allocatorIS2_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIhhEENS_22__unordered_map_hasherIhS2_NS_4hashIhEENS_8equal_toIhEELb1EEENS_21__unordered_map_equalIhS2_S7_S5_Lb1EEENS_9allocatorIS2_EEED2Ev
+ __ZZ52-[HSTTelemetryAnalyticsStage _initializeReportIdMap]E9reportIds
+ ___49-[HSTTelemetryAnalyticsStage _setupPeriodicTimer]_block_invoke
+ ___58-[HSTTelemetryAnalyticsStage _sendAnalyticsEvent:payload:]_block_invoke
+ ___block_descriptor_40_ea8_32s_e19_"NSDictionary"8?0ls32l8
+ _objc_msgSend$_initializeReportIdMap
+ _objc_msgSend$_logPathReports
+ _objc_msgSend$_sendAnalyticsEvent:payload:
+ _objc_msgSend$_setupPeriodicTimer
+ _objc_msgSend$_trackReportID:
- __Block_byref_object_copy_.420
- __Block_byref_object_dispose_.421
CStrings:
+ "9130.2"
+ "@\"NSDictionary\"8@?0"
+ "Deallocating telemetry analytics stage"
+ "HSTTelemetryAnalyticsStage"
+ "Sending analytics event: %{public}@"
+ "Telemetry analytics stage scheduling periodic 24h logging on dispatch queue"
+ "Telemetry reporter logging found report IDs"
+ "_initializeReportIdMap"
+ "_logPathReports"
+ "_periodicTimer"
+ "_receivedMask"
+ "_reportIdToBitMap"
+ "_sendAnalyticsEvent:payload:"
+ "_setupPeriodicTimer"
+ "_trackReportID:"
+ "b"
+ "com.apple.HID.multitouchPathsReportIDUsage"
+ "reportID"
+ "reportID_value"
+ "{unordered_map<unsigned char, unsigned char, std::hash<unsigned char>, std::equal_to<unsigned char>, std::allocator<std::pair<const unsigned char, unsigned char>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned char, unsigned char>, std::__unordered_map_hasher<unsigned char, std::__hash_value_type<unsigned char, unsigned char>, std::hash<unsigned char>, std::equal_to<unsigned char>>, std::__unordered_map_equal<unsigned char, std::__hash_value_type<unsigned char, unsigned char>, std::equal_to<unsigned char>, std::hash<unsigned char>>, std::allocator<std::__hash_value_type<unsigned char, unsigned char>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned char, unsigned char>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned char, unsigned char>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned char, unsigned char>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned char, unsigned char>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
- "9130.1"

```
