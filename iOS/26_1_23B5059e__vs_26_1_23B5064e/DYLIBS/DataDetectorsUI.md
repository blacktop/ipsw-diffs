## DataDetectorsUI

> `/System/Library/PrivateFrameworks/DataDetectorsUI.framework/DataDetectorsUI`

```diff

-598.0.0.0.0
-  __TEXT.__text: 0x52b54
-  __TEXT.__auth_stubs: 0xec0
+599.0.0.0.0
+  __TEXT.__text: 0x53804
+  __TEXT.__auth_stubs: 0xed0
   __TEXT.__delay_stubs: 0x2c
   __TEXT.__delay_helper: 0x1400
-  __TEXT.__objc_methlist: 0x4c48
+  __TEXT.__objc_methlist: 0x4d40
   __TEXT.__const: 0x270
   __TEXT.__oslogstring: 0x2198
-  __TEXT.__gcc_except_tab: 0xd68
-  __TEXT.__cstring: 0x5bb5
+  __TEXT.__gcc_except_tab: 0xd98
+  __TEXT.__cstring: 0x5c85
   __TEXT.__ustring: 0x4aa
   __TEXT.__constg_swiftt: 0x110
   __TEXT.__swift5_typeref: 0x4a

   __TEXT.__swift5_fieldmd: 0x54
   __TEXT.__swift5_capture: 0x10
   __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0x1440
-  __TEXT.__objc_classname: 0xc13
-  __TEXT.__objc_methname: 0xbbb5
-  __TEXT.__objc_methtype: 0x36d5
-  __TEXT.__objc_stubs: 0xabe0
+  __TEXT.__unwind_info: 0x1490
+  __TEXT.__objc_classname: 0xc33
+  __TEXT.__objc_methname: 0xbe07
+  __TEXT.__objc_methtype: 0x36f8
+  __TEXT.__objc_stubs: 0xae60
   __DATA_CONST.__got: 0xa80
-  __DATA_CONST.__const: 0xdf0
-  __DATA_CONST.__objc_classlist: 0x338
+  __DATA_CONST.__const: 0xea0
+  __DATA_CONST.__objc_classlist: 0x340
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3300
+  __DATA_CONST.__objc_selrefs: 0x3398
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_classrefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x1d8
+  __DATA_CONST.__objc_superrefs: 0x1e0
   __DATA_CONST.__objc_arraydata: 0x1638
-  __AUTH_CONST.__auth_got: 0x778
-  __AUTH_CONST.__const: 0x2e8
-  __AUTH_CONST.__cfstring: 0x65e0
-  __AUTH_CONST.__objc_const: 0x7968
+  __AUTH_CONST.__auth_got: 0x780
+  __AUTH_CONST.__const: 0x308
+  __AUTH_CONST.__cfstring: 0x6740
+  __AUTH_CONST.__objc_const: 0x7b40
   __AUTH_CONST.__objc_intobj: 0x198
   __AUTH_CONST.__objc_arrayobj: 0xde0
   __AUTH_CONST.__objc_doubleobj: 0x2f0
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0x1068
+  __AUTH.__objc_data: 0x10b8
   __AUTH.__data: 0x1a0
-  __DATA.__objc_ivar: 0x484
+  __DATA.__objc_ivar: 0x4a0
   __DATA.__data: 0xaa8
   __DATA.__bss: 0x20
   __DATA_DIRTY.__objc_data: 0xfa0
-  __DATA_DIRTY.__bss: 0x148
+  __DATA_DIRTY.__bss: 0x158
   - /System/Library/Frameworks/BusinessChat.framework/BusinessChat
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/ContactsUI.framework/ContactsUI

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 423E04B0-F5FF-313A-8E88-DDF23D53ACC9
-  Functions: 1849
-  Symbols:   7110
-  CStrings:  4291
+  UUID: A51996F9-383C-3A3B-9B59-FFC8042C82CD
+  Functions: 1877
+  Symbols:   7206
+  CStrings:  4349
 
Symbols:
+ -[DDAction analyticsReporter]
+ -[DDAction setAnalyticsReporter:]
+ -[DDActionGroup enumerateActionsUsingBlock:]
+ -[DDDataDetectorInterceptReporter appleSupport]
+ -[DDDataDetectorInterceptReporter contact]
+ -[DDDataDetectorInterceptReporter eventRepresentation]
+ -[DDDataDetectorInterceptReporter firstShownOption]
+ -[DDDataDetectorInterceptReporter init]
+ -[DDDataDetectorInterceptReporter logForAction:]
+ -[DDDataDetectorInterceptReporter log]
+ -[DDDataDetectorInterceptReporter log].cold.1
+ -[DDDataDetectorInterceptReporter savedContact]
+ -[DDDataDetectorInterceptReporter secondShownOption]
+ -[DDDataDetectorInterceptReporter selectedOption]
+ -[DDDataDetectorInterceptReporter setAppleSupport:]
+ -[DDDataDetectorInterceptReporter setContact:]
+ -[DDDataDetectorInterceptReporter setFirstShownOption:]
+ -[DDDataDetectorInterceptReporter setSavedContact:]
+ -[DDDataDetectorInterceptReporter setSecondShownOption:]
+ -[DDDataDetectorInterceptReporter setSelectedOption:]
+ -[DDDataDetectorInterceptReporter setShownOptions:]
+ -[DDDataDetectorInterceptReporter stringForOption:]
+ -[DDPersonAction _trackAppleSupportAnalytics:]
+ -[DDPersonAction dealloc]
+ GCC_except_table138
+ _AnalyticsSendEventLazy
+ _OBJC_CLASS_$_DDDataDetectorInterceptReporter
+ _OBJC_IVAR_$_DDAction._analyticsReporter
+ _OBJC_IVAR_$_DDDataDetectorInterceptReporter._appleSupport
+ _OBJC_IVAR_$_DDDataDetectorInterceptReporter._contact
+ _OBJC_IVAR_$_DDDataDetectorInterceptReporter._firstShownOption
+ _OBJC_IVAR_$_DDDataDetectorInterceptReporter._savedContact
+ _OBJC_IVAR_$_DDDataDetectorInterceptReporter._secondShownOption
+ _OBJC_IVAR_$_DDDataDetectorInterceptReporter._selectedOption
+ _OBJC_IVAR_$_DDPersonAction._analyticsReporter
+ _OBJC_METACLASS_$_DDDataDetectorInterceptReporter
+ _OUTLINED_FUNCTION_6
+ __OBJC_$_INSTANCE_METHODS_DDDataDetectorInterceptReporter
+ __OBJC_$_INSTANCE_VARIABLES_DDDataDetectorInterceptReporter
+ __OBJC_$_PROP_LIST_DDDataDetectorInterceptReporter
+ __OBJC_CLASS_RO_$_DDDataDetectorInterceptReporter
+ __OBJC_METACLASS_RO_$_DDDataDetectorInterceptReporter
+ ___38-[DDDataDetectorInterceptReporter log]_block_invoke
+ ___38-[DDDataDetectorInterceptReporter log]_block_invoke_2
+ ___46-[DDPersonAction _trackAppleSupportAnalytics:]_block_invoke
+ ___46-[DDPersonAction _trackAppleSupportAnalytics:]_block_invoke_2
+ ___analyticsQueue_block_invoke
+ ___block_descriptor_40_e8_32s_e18_v16?0"DDAction"8ls32l8
+ ___block_descriptor_40_e8_32s_e19_"NSDictionary"8?0ls32l8
+ ___block_descriptor_48_e8_32s40r_e18_v16?0"DDAction"8lr40l8s32l8
+ _objc_msgSend$_trackAppleSupportAnalytics:
+ _objc_msgSend$analyticsReporter
+ _objc_msgSend$appleSupport
+ _objc_msgSend$eventRepresentation
+ _objc_msgSend$firstShownOption
+ _objc_msgSend$log
+ _objc_msgSend$logForAction:
+ _objc_msgSend$numberWithInteger:
+ _objc_msgSend$savedContact
+ _objc_msgSend$secondShownOption
+ _objc_msgSend$selectedOption
+ _objc_msgSend$setAnalyticsReporter:
+ _objc_msgSend$setAppleSupport:
+ _objc_msgSend$setContact:
+ _objc_msgSend$setFirstShownOption:
+ _objc_msgSend$setSavedContact:
+ _objc_msgSend$setSecondShownOption:
+ _objc_msgSend$setSelectedOption:
+ _objc_msgSend$setShownOptions:
+ _objc_msgSend$stringForOption:
- -[DDSupportFlowAction queryString]
- -[DDSupportFlowAction setQueryString:]
- GCC_except_table136
- _OBJC_IVAR_$_DDSupportFlowAction._queryString
- __OBJC_$_PROP_LIST_DDSupportFlowAction
CStrings:
+ "6B"
+ "@\"DDDataDetectorInterceptReporter\""
+ "@\"NSDictionary\"8@?0"
+ "DDDataDetectorInterceptReporter"
+ "T@\"DDDataDetectorInterceptReporter\",&,N,V_analyticsReporter"
+ "TB,N,V_appleSupport"
+ "TB,N,V_contact"
+ "TB,N,V_savedContact"
+ "Tq,N,V_firstShownOption"
+ "Tq,N,V_secondShownOption"
+ "Tq,N,V_selectedOption"
+ "_analyticsReporter"
+ "_appleSupport"
+ "_firstShownOption"
+ "_savedContact"
+ "_secondShownOption"
+ "_selectedOption"
+ "_trackAppleSupportAnalytics:"
+ "analyticsReporter"
+ "appleSupport"
+ "apple_support"
+ "call"
+ "com.apple.datadetectors.analytics"
+ "com.apple.phone.data_detector"
+ "dayViewControllerShouldDrawTodaySynchronously:"
+ "eventRepresentation"
+ "firstShownOption"
+ "hmt"
+ "log"
+ "logForAction:"
+ "numberWithInteger:"
+ "other"
+ "savedContact"
+ "saved_contact"
+ "secondShownOption"
+ "selectedOption"
+ "selected_option"
+ "setAnalyticsReporter:"
+ "setAppleSupport:"
+ "setFirstShownOption:"
+ "setSavedContact:"
+ "setSecondShownOption:"
+ "setSelectedOption:"
+ "setShownOptions:"
+ "shown_option_1"
+ "shown_option_2"
+ "stringForOption:"
+ "v16@?0@\"DDAction\"8"
+ "website"
- "6A"
- "T@\"NSString\",&,V_queryString"
- "dayViewControllerShouldDrawSynchronously:"

```
