## ndoagent

> `/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/ndoagent`

```diff

-405.0.0.0.0
-  __TEXT.__text: 0x10518
-  __TEXT.__auth_stubs: 0x5d0
-  __TEXT.__objc_stubs: 0x21a0
-  __TEXT.__objc_methlist: 0x878
+407.8.0.0.0
+  __TEXT.__text: 0x113bc
+  __TEXT.__auth_stubs: 0x5e0
+  __TEXT.__objc_stubs: 0x23c0
+  __TEXT.__objc_methlist: 0x940
   __TEXT.__const: 0x30
-  __TEXT.__cstring: 0x13cf
-  __TEXT.__oslogstring: 0x1cc8
-  __TEXT.__objc_classname: 0x20c
-  __TEXT.__objc_methname: 0x2117
-  __TEXT.__objc_methtype: 0x697
-  __TEXT.__gcc_except_tab: 0x3d4
+  __TEXT.__cstring: 0x1400
+  __TEXT.__oslogstring: 0x1dfd
+  __TEXT.__objc_classname: 0x21c
+  __TEXT.__objc_methname: 0x2405
+  __TEXT.__objc_methtype: 0x706
+  __TEXT.__gcc_except_tab: 0x3ec
   __TEXT.__ustring: 0x30
   __TEXT.__dlopen_cstrs: 0x50
-  __TEXT.__unwind_info: 0x3cc
-  __DATA_CONST.__auth_got: 0x2f8
+  __TEXT.__unwind_info: 0x40c
+  __DATA_CONST.__auth_got: 0x300
   __DATA_CONST.__got: 0xf0
-  __DATA_CONST.__const: 0x7f8
-  __DATA_CONST.__cfstring: 0xb40
-  __DATA_CONST.__objc_classlist: 0x90
+  __DATA_CONST.__const: 0x958
+  __DATA_CONST.__cfstring: 0xbe0
+  __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0xd8
-  __DATA_CONST.__objc_arraydata: 0x80
+  __DATA_CONST.__objc_arraydata: 0x90
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x41d8
-  __DATA.__objc_selrefs: 0x938
+  __DATA.__objc_const: 0x4378
+  __DATA.__objc_selrefs: 0x9d8
   __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x1a8
+  __DATA.__objc_classrefs: 0x1c0
   __DATA.__objc_superrefs: 0x28
-  __DATA.__objc_ivar: 0x58
-  __DATA.__objc_data: 0x5a0
+  __DATA.__objc_ivar: 0x68
+  __DATA.__objc_data: 0x5f0
   __DATA.__data: 0x240
-  __DATA.__bss: 0x28
+  __DATA.__bss: 0x40
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 290
-  Symbols:   171
-  CStrings:  788
+  Functions: 313
+  Symbols:   174
+  CStrings:  807
 
Symbols:
+ _OBJC_CLASS_$_NDODeviceSection
+ _OBJC_CLASS_$_NSSet
+ _dispatch_sync
CStrings:
+ "\x13"
+ "%{public}s"
+ "%{public}s Disable cache for (%{private}@)"
+ "%{public}s Failed to create device (%{private}@)"
+ "%{public}s got response"
+ "-[NDOWarrantyDownloader _downloadDeviceListForLocalDevices:sessionID:completionHandler:]"
+ "-[NDOWarrantyDownloader _downloadDeviceListForLocalDevices:sessionID:completionHandler:]_block_invoke"
+ "-[NDOWarrantyDownloader downloadDeviceForLocalDevices:sessionID:completionHandler:]"
+ "@\"NSMutableURLRequest\""
+ "@40@0:8@16@24@32"
+ "B32@?0@\"NDODeviceSection\"8Q16^B24"
+ "Device list download skipped server due to server version"
+ "DeviceListURL"
+ "Do not cache SN list queue"
+ "NDODownloader"
+ "NOT caching warranty for locale: '%@', version: %@ (sn: %{private}@)"
+ "Request complete: %ld : %@"
+ "Starting request"
+ "T@\"NSMutableURLRequest\",&,V_request"
+ "T@\"NSString\",&,V_callingProcessBundleID"
+ "T@\"NSString\",&,V_sessionID"
+ "Ti,V_retries"
+ "_downloadDeviceListForLocalDevices:sessionID:completionHandler:"
+ "_downloadDeviceListFromServerURL:serialNumber:localDevices:sessionID:withRetries:completionBlock:"
+ "_request"
+ "_retries"
+ "_sessionID"
+ "addDevice:"
+ "arrayWithCapacity:"
+ "caching warranty for locale: '%@', version: %@ (sn: %{private}@)"
+ "cachingPolicy"
+ "callingProcessBundleID"
+ "category"
+ "categoryLabel"
+ "deviceList"
+ "deviceWithCBDevice:"
+ "deviceWithCBDevice:isVisibleInCC:"
+ "deviceWithDeviceListDevice:"
+ "downloadDeviceForLocalDevices:sessionID:completionHandler:"
+ "downloadWithRetryCount:prepareBlock:completion:"
+ "getDeviceListForLocalDevices:sessionID:withReply:"
+ "https://cdsassets.apple.com/live/ondevice/plist/ndoV3.plist"
+ "https://sse-ws-p189.apple.com/api/v1/coverage/deviceList"
+ "indexOfObjectPassingTest:"
+ "initWithLabel:identifier:"
+ "initWithURL %{private}@"
+ "initWithURL:callingProcessBundleID:sessionID:"
+ "objectAtIndexedSubscript:"
+ "request"
+ "retries"
+ "sessionID"
+ "setCallingProcessBundleID:"
+ "setClasses:forSelector:argumentIndex:ofReply:"
+ "setRequest:"
+ "setRetries:"
+ "setSessionID:"
+ "setWithObjects:"
+ "v16@?0@\"NSMutableURLRequest\"8"
+ "v20@?0B8@\"NSArray\"12"
+ "v36@0:8i16@?20@?28"
+ "v40@0:8@\"NSArray\"16@\"NSString\"24@?<v@?@\"NSArray\">32"
- "?"
- "ATVRemote1,1"
- "ATVRemote1,2"
- "AirPods1,1"
- "AirPods1,3"
- "AirPodsPro1,1"
- "ApGn"
- "AppleTV11,2"
- "AppleTV5,3"
- "AppleTV6,2"
- "AudioAccessory1,1"
- "AudioAccessory1,2"
- "AudioAccessory5,1"
- "BeatsSolo3,1"
- "BeatsSoloPro1,1"
- "BeatsStudio3,2"
- "BeatsStudioBuds1,1"
- "BeatsStudioBuds1,2"
- "BeatsStudioPro1,1"
- "BeatsX1,1"
- "Device1,21760"
- "Device1,8202"
- "Device1,8208"
- "Device1,8210"
- "Device1,8211"
- "Device1,8212"
- "Device1,8213"
- "Device1,8216"
- "Device1,8228"
- "HeGn"
- "Invalid"
- "PowerBeats3,1"
- "Powerbeats4,1"
- "PowerbeatsPro1,1"
- "caching warranty for locale: '%@', version: %@"
- "deviceWithName:serialNumber:activationDate:deviceType:productID:productName:isVisibleInCC:"
- "https://cdsassets.apple.com/library/APPLE/asset/ndoV3.plist"
- "load warranty status: %ld : %@"
- "productID"
- "productName"
- "stringWithUTF8String:"

```
