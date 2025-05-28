## ndoagent

> `/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/ndoagent`

```diff

-407.8.0.0.0
-  __TEXT.__text: 0x113bc
-  __TEXT.__auth_stubs: 0x5e0
-  __TEXT.__objc_stubs: 0x23c0
-  __TEXT.__objc_methlist: 0x940
+407.15.0.0.0
+  __TEXT.__text: 0x11a70
+  __TEXT.__auth_stubs: 0x5c0
+  __TEXT.__objc_stubs: 0x2540
+  __TEXT.__objc_methlist: 0xa08
   __TEXT.__const: 0x30
-  __TEXT.__cstring: 0x1400
-  __TEXT.__oslogstring: 0x1dfd
+  __TEXT.__cstring: 0x1459
+  __TEXT.__oslogstring: 0x1e53
   __TEXT.__objc_classname: 0x21c
-  __TEXT.__objc_methname: 0x2405
-  __TEXT.__objc_methtype: 0x706
-  __TEXT.__gcc_except_tab: 0x3ec
+  __TEXT.__objc_methname: 0x2587
+  __TEXT.__objc_methtype: 0x757
+  __TEXT.__gcc_except_tab: 0x408
   __TEXT.__ustring: 0x30
   __TEXT.__dlopen_cstrs: 0x50
-  __TEXT.__unwind_info: 0x40c
-  __DATA_CONST.__auth_got: 0x300
-  __DATA_CONST.__got: 0xf0
+  __TEXT.__unwind_info: 0x42c
+  __DATA_CONST.__auth_got: 0x2f0
+  __DATA_CONST.__got: 0xe8
   __DATA_CONST.__const: 0x958
-  __DATA_CONST.__cfstring: 0xbe0
+  __DATA_CONST.__cfstring: 0xc00
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30

   __DATA_CONST.__objc_intobj: 0xd8
   __DATA_CONST.__objc_arraydata: 0x90
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x4378
-  __DATA.__objc_selrefs: 0x9d8
+  __DATA.__objc_const: 0x45f8
+  __DATA.__objc_selrefs: 0xa30
   __DATA.__objc_protorefs: 0x8
   __DATA.__objc_classrefs: 0x1c0
   __DATA.__objc_superrefs: 0x28
-  __DATA.__objc_ivar: 0x68
+  __DATA.__objc_ivar: 0x70
   __DATA.__objc_data: 0x5f0
   __DATA.__data: 0x240
   __DATA.__bss: 0x40

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 313
-  Symbols:   174
-  CStrings:  807
+  Functions: 330
+  Symbols:   171
+  CStrings:  827
 
Symbols:
- _XPC_ACTIVITY_CHECK_IN
- _xpc_activity_register
- _xpc_activity_set_state
CStrings:
+ "%{public}s: for conversion outreach %@"
+ "+[NDOConversionOutreachActivity outreachActivityForSerialNumber:]"
+ "-%@"
+ "-[NDOWarrantyDownloader _downloadDeviceListForLocalDevices:sessionID:params:completionHandler:]"
+ "-[NDOWarrantyDownloader _downloadDeviceListForLocalDevices:sessionID:params:completionHandler:]_block_invoke"
+ "-[NDOWarrantyDownloader downloadDeviceForLocalDevices:sessionID:params:completionHandler:]"
+ "<unknown-unknown>"
+ "@\"NSArray\""
+ "DeviceListRequestBody error - No primary iCloud account, can't sign this request"
+ "Not Scheduling conversion outreach %@ (%@)"
+ "Scheduling conversion outreach %@ (%@)"
+ "T@\"NSString\",&,V_warrantySN"
+ "_appleIDDeviceList"
+ "_downloadDeviceListForLocalDevices:sessionID:params:completionHandler:"
+ "_downloadDeviceListFromServerURL attempt (%d/%d)"
+ "_downloadDeviceListFromServerURL:serialNumber:localDevices:sessionID:params:withRetries:completionBlock:"
+ "_scheduleConversionOutreachIfRequiredForWarranty:serialNumber:andCachedWarranty:"
+ "_warrantySN"
+ "agsULUrl"
+ "appleIDDevices"
+ "dictionaryWithCapacity:"
+ "downloadDeviceForLocalDevices:sessionID:params:completionHandler:"
+ "getDeviceListForLocalDevices:sessionID:params:withReply:"
+ "getScheduledActivityDateAndKey"
+ "hasPrefix:"
+ "ndo_setDeviceListRequestBodyWithSerialNumber:localDevices:primaryAccount:"
+ "newSchedulerWithActivityDelegate:forDate:"
+ "outreachActivityForSerialNumber:"
+ "scheduled '%@ (%@)' with delay: %.02f (%@)"
+ "setAppleIDDeviceList:"
+ "setWarrantySN:"
+ "stringByAppendingFormat:"
+ "uuid"
+ "v28@?0B8@\"NSArray\"12@\"NSString\"20"
+ "v40@0:8@16@24@32"
+ "v48@0:8@\"NSArray\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSArray\"@\"NSString\">40"
+ "v68@0:8@16@24@32@40@48i56@?60"
+ "warrantySN"
+ "{?=@@}16@0:8"
- "-[NDOWarrantyDownloader _downloadDeviceListForLocalDevices:sessionID:completionHandler:]"
- "-[NDOWarrantyDownloader _downloadDeviceListForLocalDevices:sessionID:completionHandler:]_block_invoke"
- "-[NDOWarrantyDownloader downloadDeviceForLocalDevices:sessionID:completionHandler:]"
- "<unknown>"
- "ConversionOutreachScheduledDate"
- "Re-scheduling conversion outreach %@"
- "Skipping re-scheduling conversion outreach as there is already one."
- "XPC activity: '%@' removed: %d"
- "_downloadDeviceListForLocalDevices:sessionID:completionHandler:"
- "_downloadDeviceListFromServerURL:serialNumber:localDevices:sessionID:withRetries:completionBlock:"
- "_scheduleConversionOutreachIfRequiredForWarranty:andCachedWarranty:"
- "downloadDeviceForLocalDevices:sessionID:completionHandler:"
- "getDeviceListForLocalDevices:sessionID:withReply:"
- "removeScheduledActivity"
- "scheduled '%@' with delay: %.02f (%@)"
- "scheduling conversion outreach %@"
- "v20@?0B8@\"NSArray\"12"
- "v32@0:8@16@24"
- "v40@0:8@\"NSArray\"16@\"NSString\"24@?<v@?@\"NSArray\">32"

```
