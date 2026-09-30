## MobileTimer

> `/System/Library/PrivateFrameworks/MobileTimer.framework/MobileTimer`

```diff

-  __TEXT.__text: 0x1352a4
-  __TEXT.__objc_methlist: 0xe9fc
-  __TEXT.__const: 0x21c0
+  __TEXT.__text: 0x135d4c
+  __TEXT.__objc_methlist: 0xea84
+  __TEXT.__const: 0x21d0
   __TEXT.__gcc_except_tab: 0x1228
-  __TEXT.__cstring: 0x99b2
-  __TEXT.__oslogstring: 0x12d63
+  __TEXT.__cstring: 0x99c2
+  __TEXT.__oslogstring: 0x12d93
   __TEXT.__dlopen_cstrs: 0x9dd
   __TEXT.__ustring: 0x2c
-  __TEXT.__swift5_typeref: 0x1134
+  __TEXT.__swift5_typeref: 0x113c
   __TEXT.__swift5_reflstr: 0x4ad
   __TEXT.__swift5_assocty: 0x198
   __TEXT.__constg_swiftt: 0x9f8
   __TEXT.__swift5_fieldmd: 0x5cc
   __TEXT.__swift5_proto: 0xc4
   __TEXT.__swift5_types: 0xac
-  __TEXT.__swift5_capture: 0x1cc4
+  __TEXT.__swift5_capture: 0x1d20
   __TEXT.__swift5_builtin: 0x8c
-  __TEXT.__swift_as_entry: 0x1b0
-  __TEXT.__swift_as_ret: 0x1b4
+  __TEXT.__swift_as_entry: 0x1b4
+  __TEXT.__swift_as_ret: 0x1b8
   __TEXT.__swift_as_cont: 0x4d0
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x5988
-  __TEXT.__eh_frame: 0x5060
+  __TEXT.__unwind_info: 0x59a0
+  __TEXT.__eh_frame: 0x5098
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x3b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x67f8
+  __DATA_CONST.__objc_selrefs: 0x6830
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x460
   __DATA_CONST.__objc_arraydata: 0x38
   __DATA_CONST.__got: 0xd20
-  __AUTH_CONST.__const: 0x5b88
+  __AUTH_CONST.__const: 0x5c68
   __AUTH_CONST.__cfstring: 0x7520
-  __AUTH_CONST.__objc_const: 0x2c208
+  __AUTH_CONST.__objc_const: 0x2c238
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__objc_floatobj: 0x10

   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0xe68
   __AUTH.__objc_data: 0x3898
-  __AUTH.__data: 0x7b8
-  __DATA.__objc_ivar: 0xa18
+  __AUTH.__data: 0x7b0
+  __DATA.__objc_ivar: 0xa1c
   __DATA.__data: 0x30b0
   __DATA.__common: 0x90
   __DATA.__bss: 0x1d10

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 7870
-  Symbols:   20950
-  CStrings:  3787
+  Functions: 7893
+  Symbols:   20991
+  CStrings:  3788
 
Sections:
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_fieldmd : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __TEXT.__swift5_protos : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_floatobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ +[MTAnalyticsCoordinator testCoordinatorWithAlarmStorage:persistence:reportsManager:currentDateProvider:]
+ -[MTAnalyticsCoordinator currentDateProvider]
+ -[MTAnalyticsCoordinator fetchPendingReportConcernsWithCompletion:]
+ -[MTAnalyticsCoordinator initWithAlarmStorage:dataStore:persistence:reportsManager:currentDateProvider:]
+ -[MTAnalyticsCoordinator isDataStoreReady]
+ -[MTAnalyticsCoordinator loadDataStore]
+ -[MTAnalyticsCoordinator saveReport:completion:]
+ -[MTAnalyticsCoordinator setCurrentDateProvider:]
+ -[MTStoredReportValue isValid]
+ _OBJC_IVAR_$_MTAnalyticsCoordinator._currentDateProvider
+ __OBJC_$_CLASS_METHODS_MTAnalyticsCoordinator
+ ___104-[MTAnalyticsCoordinator initWithAlarmStorage:dataStore:persistence:reportsManager:currentDateProvider:]_block_invoke
+ ___48-[MTAnalyticsCoordinator saveReport:completion:]_block_invoke
+ ___67-[MTAnalyticsCoordinator fetchPendingReportConcernsWithCompletion:]_block_invoke
+ ___69-[MTAnalyticsCoordinator initWithAlarmStorage:dataStore:persistence:]_block_invoke
+ ___block_descriptor_40_e8_32s_e50_24?0"<MTStoredReport>"8"NSMutableDictionary"16ls32l8
+ ___swift_closure_destructor.104Tm
+ ___swift_closure_destructor.118Tm
+ ___swift_closure_destructor.151Tm
+ ___swift_closure_destructor.157Tm
+ ___swift_closure_destructor.166Tm
+ ___swift_closure_destructor.175Tm
+ ___swift_closure_destructor.184Tm
+ ___swift_closure_destructor.193Tm
+ ___swift_closure_destructor.202Tm
+ ___swift_closure_destructor.211Tm
+ ___swift_closure_destructor.281Tm
+ ___swift_closure_destructor.301Tm
+ ___swift_closure_destructor.310Tm
+ ___swift_closure_destructor.337Tm
+ ___swift_closure_destructor.396Tm
+ ___swift_closure_destructor.423Tm
+ ___swift_closure_destructor.429Tm
+ ___swift_closure_destructor.471Tm
+ ___swift_closure_destructor.77Tm
+ ___swift_closure_destructor.86Tm
+ ___swift_closure_destructor.95Tm
+ _objc_msgSend$initWithAlarmStorage:dataStore:persistence:reportsManager:currentDateProvider:
+ _objc_msgSend$savePendingReportWithConversion:completion:
+ _objc_msgSend$saveReport:completion:
+ _symbolic Ieg_Sg
- ___37-[MTAnalyticsCoordinator saveReport:]_block_invoke
- ___block_descriptor_40_e8_32s_e44_24?0"MTCDReport"8"NSMutableDictionary"16ls32l8
- ___swift_closure_destructor.113Tm
- ___swift_closure_destructor.152Tm
- ___swift_closure_destructor.161Tm
- ___swift_closure_destructor.165Tm
- ___swift_closure_destructor.179Tm
- ___swift_closure_destructor.188Tm
- ___swift_closure_destructor.197Tm
- ___swift_closure_destructor.206Tm
- ___swift_closure_destructor.276Tm
- ___swift_closure_destructor.296Tm
- ___swift_closure_destructor.305Tm
- ___swift_closure_destructor.332Tm
- ___swift_closure_destructor.391Tm
- ___swift_closure_destructor.418Tm
- ___swift_closure_destructor.424Tm
- ___swift_closure_destructor.466Tm
- ___swift_closure_destructor.72Tm
- ___swift_closure_destructor.81Tm
- ___swift_closure_destructor.90Tm
- ___swift_closure_destructor.99Tm
- _objc_msgSend$savePendingReportWithConversion:
CStrings:
+ "%{public}@ skipping report with invalid date: %{public}@"
+ "@24@?0@\"<MTStoredReport>\"8@\"NSMutableDictionary\"16"
- "@24@?0@\"MTCDReport\"8@\"NSMutableDictionary\"16"

```
