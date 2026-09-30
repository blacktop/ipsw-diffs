## HealthRecordsPlugin

> `/System/Library/Health/Plugins/HealthRecordsPlugin.bundle/HealthRecordsPlugin`

```diff

-6200.2.12.0.0
-  __TEXT.__text: 0xa7f1c
+6200.2.14.2.5
+  __TEXT.__text: 0xa8638
   __TEXT.__auth_stubs: 0xf60
-  __TEXT.__objc_stubs: 0x11aa0
-  __TEXT.__objc_methlist: 0x78cc
-  __TEXT.__objc_methname: 0x1b076
-  __TEXT.__objc_classname: 0x1889
-  __TEXT.__objc_methtype: 0x31e0
+  __TEXT.__objc_stubs: 0x11b40
+  __TEXT.__objc_methlist: 0x795c
+  __TEXT.__objc_methname: 0x1b19b
+  __TEXT.__objc_classname: 0x18c7
+  __TEXT.__objc_methtype: 0x321c
   __TEXT.__const: 0x292
   __TEXT.__gcc_except_tab: 0x2000
-  __TEXT.__cstring: 0x9265
-  __TEXT.__oslogstring: 0xecce
+  __TEXT.__cstring: 0x9345
+  __TEXT.__oslogstring: 0xee5f
   __TEXT.__ustring: 0x7e
   __TEXT.__constg_swiftt: 0x38
   __TEXT.__swift5_typeref: 0x105

   __TEXT.__swift5_types: 0x4
   __TEXT.__swift_as_entry: 0x10
   __TEXT.__swift_as_ret: 0x8
-  __TEXT.__unwind_info: 0x2670
+  __TEXT.__unwind_info: 0x2688
   __TEXT.__eh_frame: 0x210
   __DATA_CONST.__auth_got: 0x7c0
   __DATA_CONST.__got: 0xf38
   __DATA_CONST.__auth_ptr: 0x20
   __DATA_CONST.__const: 0x37f0
-  __DATA_CONST.__cfstring: 0x66e0
-  __DATA_CONST.__objc_classlist: 0x410
+  __DATA_CONST.__cfstring: 0x6760
+  __DATA_CONST.__objc_classlist: 0x418
   __DATA_CONST.__objc_catlist: 0x120
-  __DATA_CONST.__objc_protolist: 0x140
+  __DATA_CONST.__objc_protolist: 0x148
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x2f0
+  __DATA_CONST.__objc_superrefs: 0x2f8
   __DATA_CONST.__objc_intobj: 0x510
   __DATA_CONST.__objc_arraydata: 0x150
   __DATA_CONST.__objc_arrayobj: 0x108
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA.__objc_const: 0xb598
-  __DATA.__objc_selrefs: 0x50f0
-  __DATA.__objc_ivar: 0x5e8
-  __DATA.__objc_data: 0x2908
-  __DATA.__data: 0xf58
+  __DATA.__objc_const: 0xb7c0
+  __DATA.__objc_selrefs: 0x5130
+  __DATA.__objc_ivar: 0x604
+  __DATA.__objc_data: 0x2958
+  __DATA.__data: 0xfb8
   __DATA.__bss: 0x50
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 3D4D38CA-C5FF-3908-8881-A9D51F8029D4
-  Functions: 3207
-  Symbols:   1027
-  CStrings:  6268
+  UUID: A8B3DD75-E36B-3D1E-85C2-D2954739635E
+  Functions: 3216
+  Symbols:   1029
+  CStrings:  6301
 
Symbols:
+ _OBJC_CLASS_$_HDClinicalOptInStudyUpload
+ _OBJC_METACLASS_$_HDClinicalOptInStudyUpload
CStrings:
+ "%{public}@: already triggered, ignoring, do not trigger more than once"
+ "%{public}@: opt-in data collection activity should be deferred"
+ "%{public}@: opt-in data collection activity triggered"
+ "%{public}@: opt-in data collection is not enabled by the user"
+ "%{public}@: opt-in data upload trigger <%p> completed"
+ "%{public}@: triggering opt-in data upload <%p>"
+ "4"
+ "Aborting upload of analytics health wrap messages"
+ "B24@0:8@\"HDClinicalOptInStudy\"16"
+ "HDClinicalOptInStudyUpload"
+ "HDClinicalOptInStudyUploadDelegate"
+ "Opt-in upload was asked to defer [before enabling collection]"
+ "Opt-in upload was asked to defer [before file loop]"
+ "Opt-in upload was asked to defer [before upload]"
+ "Opt-in upload was asked to defer [during file loop]"
+ "T@\"NSMutableArray\",R,N,V_currentUploads"
+ "T{os_unfair_lock_s=I},R,N,V_uploadsLock"
+ "_currentUploads"
+ "_didTrigger"
+ "_shouldAbort"
+ "_uploadSubmittedAnalyticsDataWithUploadDelegate:error:"
+ "_uploadsLock"
+ "abortCurrentUploads"
+ "clinicalOptInStudyShouldAbortUpload:"
+ "currentUploads"
+ "initWithStudy:completion:"
+ "makeObjectsPerformSelector:"
+ "shouldAbortUpload"
+ "shouldDefer"
+ "triggerOptInAnalyticsDataUploadToHealthCloudWithUploadDelegate:error:"
+ "triggerUpload"
+ "uploadsLock"
+ "{os_unfair_lock_s=I}16@0:8"
- "#"
- "_queue_triggerClinicalOptInDataUploadWithCompletion:"
- "_uploadSubmittedAnalyticsDataWithError:"
- "triggerOptInAnalyticsDataUploadToHealthCloudWithError:"

```
