## inboxupdaterd

> `/usr/libexec/inboxupdaterd`

```diff

-63.120.35.0.0
-  __TEXT.__text: 0x68014
-  __TEXT.__auth_stubs: 0x1170
-  __TEXT.__objc_stubs: 0x6400
-  __TEXT.__objc_methlist: 0x3084
-  __TEXT.__cstring: 0x3708
-  __TEXT.__objc_methname: 0x666b
+132.0.0.0.0
+  __TEXT.__text: 0x69324
+  __TEXT.__auth_stubs: 0x11c0
+  __TEXT.__objc_stubs: 0x6480
+  __TEXT.__objc_methlist: 0x30a4
+  __TEXT.__cstring: 0x37a8
+  __TEXT.__objc_methname: 0x66e0
   __TEXT.__objc_classname: 0x4f6
   __TEXT.__objc_methtype: 0x1232
-  __TEXT.__const: 0x2a81
-  __TEXT.__oslogstring: 0x62b0
+  __TEXT.__const: 0x6e70
+  __TEXT.__oslogstring: 0x635a
   __TEXT.__gcc_except_tab: 0x1548
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x16b0
-  __DATA_CONST.__auth_got: 0x8c8
+  __TEXT.__unwind_info: 0x16f0
+  __DATA_CONST.__auth_got: 0x8f0
   __DATA_CONST.__got: 0x338
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x9548
-  __DATA_CONST.__cfstring: 0x3100
+  __DATA_CONST.__const: 0xb568
+  __DATA_CONST.__cfstring: 0x31c0
   __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x98

   __DATA_CONST.__objc_arraydata: 0x4e8
   __DATA_CONST.__objc_arrayobj: 0x540
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0x7950
-  __DATA.__objc_selrefs: 0x1d10
-  __DATA.__objc_ivar: 0x324
+  __DATA.__objc_const: 0x7980
+  __DATA.__objc_selrefs: 0x1d30
+  __DATA.__objc_ivar: 0x328
   __DATA.__objc_data: 0xbe0
-  __DATA.__data: 0x1b00
+  __DATA.__data: 0x1ba8
   __DATA.__bss: 0x110
   __DATA.__common: 0x28
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/libamsupport.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8B998A28-7C24-3519-89C3-083ABDD8A281
-  Functions: 2925
-  Symbols:   391
-  CStrings:  3111
+  UUID: 0ECAFFD9-A143-3EA3-99FC-EA33187F56BD
+  Functions: 2946
+  Symbols:   396
+  CStrings:  3130
 
Symbols:
+ _arc4random_uniform
+ _ccder_blob_encode_implicit_raw_octet_string
+ _ccder_blob_encode_implicit_uint64
+ _ccder_sizeof_implicit_raw_octet_string
+ _ccder_sizeof_implicit_uint64
CStrings:
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s aks connection failed%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s bad 1%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s fail%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s ioreg: %d, boot_arg: %d%s\n"
+ "An error happened while downloading update asset"
+ "An error happened while extracting update asset"
+ "An error happened while setting up asset file"
+ "Connection retry finished with error: %{public}@, total retry count: %lu"
+ "CurrentBuildVersion"
+ "Disassociating with WiFi..."
+ "Failed to connect to wifi with error %{public}@, waiting for %us"
+ "SSUNanSubscriberDiscoveredResult"
+ "SSUWiFiInfraConnFailed"
+ "SSUWiFiInfraConnSucceeded"
+ "Subscriber"
+ "TQ,N,V_globalRetryCount"
+ "WiFiConnectRetryTotalCount"
+ "_globalRetryCount"
+ "disassociate"
+ "disassociateWithReason:"
+ "failed to open connection to %s: %d\n"
+ "failed to open userclient via %s: %d\n"
+ "globalRetryCount"
+ "setGlobalRetryCount:"
- "%s%s:%s%s%s%s%u:%s%u:%s aks connection failed%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s bad 1%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s bad 2%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s fail%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s ioreg: %d, boot_arg: %d%s\n"
- "Connection retry finished with error: %{public}@"
- "Failed to download update asset"
- "Failed to extract update asset"
- "Failed to setup asset file"
- "der_key_validate"
- "failed to open connection to %s\n"

```
