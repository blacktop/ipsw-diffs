## HealthRecordsPlugin

> `/System/Library/Health/Plugins/HealthRecordsPlugin.bundle/HealthRecordsPlugin`

```diff

-5124.0.1.3.0
-  __TEXT.__text: 0xb2240
-  __TEXT.__auth_stubs: 0xdb0
-  __TEXT.__objc_stubs: 0x13120
-  __TEXT.__objc_methlist: 0x7b9c
-  __TEXT.__objc_methname: 0x1d000
-  __TEXT.__objc_classname: 0x1c11
+5132.0.0.0.0
+  __TEXT.__text: 0xb195c
+  __TEXT.__auth_stubs: 0xda0
+  __TEXT.__objc_stubs: 0x13000
+  __TEXT.__objc_methlist: 0x7b74
+  __TEXT.__objc_methname: 0x1cf28
+  __TEXT.__objc_classname: 0x1bed
   __TEXT.__objc_methtype: 0x3563
   __TEXT.__const: 0x1f4
-  __TEXT.__gcc_except_tab: 0x2280
-  __TEXT.__cstring: 0xa149
-  __TEXT.__oslogstring: 0xeca6
+  __TEXT.__gcc_except_tab: 0x22ac
+  __TEXT.__cstring: 0xa0c5
+  __TEXT.__oslogstring: 0xeaa4
   __TEXT.__ustring: 0x7e
-  __TEXT.__unwind_info: 0x2810
-  __DATA_CONST.__auth_got: 0x6e8
-  __DATA_CONST.__got: 0xef8
+  __TEXT.__unwind_info: 0x2808
+  __DATA_CONST.__auth_got: 0x6e0
+  __DATA_CONST.__got: 0xef0
   __DATA_CONST.__const: 0x3828
-  __DATA_CONST.__cfstring: 0x7820
+  __DATA_CONST.__cfstring: 0x77a0
   __DATA_CONST.__objc_classlist: 0x4d8
   __DATA_CONST.__objc_catlist: 0x128
-  __DATA_CONST.__objc_protolist: 0x160
+  __DATA_CONST.__objc_protolist: 0x158
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x3a8
   __DATA_CONST.__objc_intobj: 0x6a8
   __DATA_CONST.__objc_arraydata: 0x1d8
   __DATA_CONST.__objc_arrayobj: 0x120
   __DATA_CONST.__objc_dictobj: 0xa0
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA.__objc_const: 0xeaf8
-  __DATA.__objc_selrefs: 0x5600
+  __DATA.__objc_const: 0xea98
+  __DATA.__objc_selrefs: 0x55b8
   __DATA.__objc_ivar: 0x714
   __DATA.__objc_data: 0x25d0
-  __DATA.__data: 0x1088
+  __DATA.__data: 0x1028
   __DATA.__bss: 0x60
   __DATA_DIRTY.__objc_data: 0xaa0
   __DATA_DIRTY.__bss: 0x10

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 3387
-  Symbols:   1090
-  CStrings:  5972
+  Functions: 3380
+  Symbols:   1088
+  CStrings:  5952
 
Symbols:
+ _OBJC_EHTYPE_$_NSException
- _HDEntityCategoryForKeyValueCategory
- _HKClinicalSharingKeyValueDomainDomainName
- _HKClinicalSharingKeyValueDomainKeyDAIData
CStrings:
+ "HDHealthRecordsPluginServer._notifyObserversAboutAccountsEvent: retrieved remote object but threw exception when trying to call `clientRemote_healthRecordsAccountsEventObserved:`: %!{(MISSING)public}@"
- "%!{(MISSING)public}@ Fetching data from KeyValueDomain for DAI data failed with error: %!{(MISSING)public}@"
- "%!{(MISSING)public}@ No pending DAI upload task"
- "%!{(MISSING)public}@ Sending upload DAI XPC request"
- "%!{(MISSING)public}@ Start observing protected database as there is a pending DAI upload task"
- "%!{(MISSING)public}@ Stop observing protected database as there is no more pending DAI upload task"
- "%!{(MISSING)public}@ failed to upload DocumentReference for DAI: %!{(MISSING)public}@"
- "%!{(MISSING)public}@: Scheduling DocumentReference for DAI upload task on maintenance coordinator with reason: %!{(MISSING)public}@"
- "ClinicalSharingDAIContentAttachmentData"
- "HDHealthRecordsPluginServer._notifyObserversAboutAccountsEvent: retrieving remote object, which must conform to HKHealthRecordsStoreClientInterface, but this object does not: %!{(MISSING)public}@"
- "HKHealthRecordsStoreClientInterface"
- "Upload DocumentReference for DAI (%!@(MISSING))"
- "_registerKVDObservation:"
- "_scheduleUploadDAIIfNeededWithReason:"
- "_unregisterKVDObservation"
- "addProtectedDataObserver:"
- "dataForKey:error:"
- "profileDidBecomeReady"
- "protectedDataDidBecomeAvailable"
- "startObservation:"
- "stopObservation:"
- "uploadDAIIfNeededWithOptions:reason:completion:"

```
