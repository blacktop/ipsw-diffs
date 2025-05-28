## CommCenterMobileHelper

> `/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenterMobileHelper`

```diff

-11305.1.0.0.0
-  __TEXT.__text: 0x48f74
-  __TEXT.__auth_stubs: 0x16c0
-  __TEXT.__objc_stubs: 0x1e40
+11523.1.0.0.0
+  __TEXT.__text: 0x4b4f8
+  __TEXT.__auth_stubs: 0x17d0
+  __TEXT.__objc_stubs: 0x1fe0
   __TEXT.__init_offsets: 0x10
-  __TEXT.__objc_methlist: 0x2ac
-  __TEXT.__gcc_except_tab: 0x59d4
-  __TEXT.__cstring: 0x4e87
-  __TEXT.__const: 0x82dd
-  __TEXT.__oslogstring: 0x26b2
+  __TEXT.__objc_methlist: 0x278
+  __TEXT.__gcc_except_tab: 0x5b2c
+  __TEXT.__cstring: 0x4f22
+  __TEXT.__const: 0x851d
+  __TEXT.__oslogstring: 0x2799
   __TEXT.__objc_classname: 0x80
-  __TEXT.__objc_methname: 0x1ab7
-  __TEXT.__objc_methtype: 0x361
-  __TEXT.__unwind_info: 0x26a0
+  __TEXT.__objc_methname: 0x1b45
+  __TEXT.__objc_methtype: 0x379
+  __TEXT.__unwind_info: 0x2660
   __TEXT.__eh_frame: 0x38
-  __DATA_CONST.__auth_got: 0xb70
-  __DATA_CONST.__got: 0x238
+  __DATA_CONST.__auth_got: 0xbf8
+  __DATA_CONST.__got: 0x248
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x3e10
-  __DATA_CONST.__cfstring: 0x3a80
+  __DATA_CONST.__const: 0x3e90
+  __DATA_CONST.__cfstring: 0x3ac0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_arraydata: 0x1428
+  __DATA_CONST.__objc_classrefs: 0x1f0
+  __DATA_CONST.__objc_superrefs: 0x20
+  __DATA_CONST.__objc_arraydata: 0x1438
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA.__objc_const: 0x860
-  __DATA.__objc_selrefs: 0x7f0
-  __DATA.__objc_classrefs: 0x1f0
-  __DATA.__objc_superrefs: 0x20
+  __DATA.__objc_selrefs: 0x850
   __DATA.__objc_ivar: 0x34
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x2c0
+  __DATA.__common: 0x48
   __DATA.__bss: 0xce0
-  __DATA.__common: 0x40
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/libprotobuf.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1957
-  Symbols:   513
-  CStrings:  1330
+  Functions: 1966
+  Symbols:   532
+  CStrings:  1360
 
Symbols:
+ __Z8asStringP8NSObject
+ __ZN4rest15read_rest_valueERNS_22logDataUsageParametersERKN3xpc6objectE
+ __ZN4rest22logDataUsageParametersC1Ebj
+ __ZNKSt3__16locale9use_facetERNS0_2idE
+ __ZNKSt3__18ios_base6getlocEv
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE3putEc
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE5flushEv
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE6sentryC1ERS3_
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE6sentryD1Ev
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEElsEd
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEElsEy
+ __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEEC2Ev
+ __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEED2Ev
+ __ZNSt3__15ctypeIcE2idE
+ __ZNSt3__16localeD1Ev
+ __ZNSt3__18ios_base33__set_badbit_and_consider_rethrowEv
+ __ZNSt3__19to_stringEi
+ __ZTTNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE
+ __ZTVNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEE
+ __ZTVNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE
+ __os_log_debug_impl
+ _memset
- __ZTI23GestaltUtilityInterface
- __ZTI29ManagedConfigurationInterface
- __os_feature_enabled_impl
CStrings:
+ " ("
+ " B"
+ " KB"
+ " MB"
+ " Unknown IN "
+ " Unknown OUT "
+ " |"
+ "%s has another lu record"
+ "%{public}s"
+ ")"
+ "/helper/requests/log_data_usage"
+ "Bundle ID"
+ "Failed to get live usage records: %@"
+ "Failed to get process record ids: %@"
+ "Home IN"
+ "Home OUT"
+ "Process"
+ "Roaming IN"
+ "Roaming OUT"
+ "T@\"NSString\",?,R,C"
+ "Total"
+ "Total cellular data usage (System with no bundle): %{public}s"
+ "Total cellular data usage (System): %{public}s"
+ "Total cellular data usage: %{public}s "
+ "com.apple.datausage.dns.multicast"
+ "executeFetchRequest:error:"
+ "fetchRequest"
+ "hasProcess == %@"
+ "kind"
+ "logPerAppUsageData_sync:withCurrentSubtag:withCallback:"
+ "mainObjectContext"
+ "procName"
+ "processPendingChanges"
+ "refreshObject:mergeChanges:"
+ "setAllocationType:"
+ "setFetchBatchSize:"
+ "setPredicate:"
+ "tag"
+ "unsignedLongLongValue"
+ "v56@0:8B16I20{function<void (bool)>={__value_func<void (bool)>={type=[24C]}^v}}24"
- "0"
- "1"
- "2"
- "@40@0:8Q16r^v24r^v32"
- "B40@0:8@16@24Q32"
- "B48@0:8@16@24Q32@40"
- "CoreTelephony"
- "DataUsageRefactor"
- "DataUsageSeedWithProcesses"
- "addUsage:forBundle:forPeriod:"
- "addUsage:forBundle:forPeriod:using:"
- "displayNameForBundle:withBuilder:"
- "initWithPeriods:andRegistry:andLogger:"
- "validateSystemService:usingBuilder:"

```
