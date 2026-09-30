## NetworkRelay

> `/System/Library/PrivateFrameworks/NetworkRelay.framework/NetworkRelay`

```diff

-673.0.0.0.0
-  __TEXT.__text: 0x6b4bc
+676.0.3.0.0
+  __TEXT.__text: 0x6c4c4
   __TEXT.__auth_stubs: 0xee0
-  __TEXT.__objc_methlist: 0x1ad4
+  __TEXT.__objc_methlist: 0x1aec
   __TEXT.__const: 0x200
   __TEXT.__gcc_except_tab: 0x8b4
-  __TEXT.__cstring: 0xe0e4
+  __TEXT.__cstring: 0xe33c
   __TEXT.__oslogstring: 0x124c
-  __TEXT.__unwind_info: 0x8f8
+  __TEXT.__unwind_info: 0x908
   __TEXT.__objc_classname: 0x362
-  __TEXT.__objc_methname: 0x4948
+  __TEXT.__objc_methname: 0x4995
   __TEXT.__objc_methtype: 0x797
   __TEXT.__objc_stubs: 0x2b20
   __DATA_CONST.__got: 0x260
-  __DATA_CONST.__const: 0xdd8
+  __DATA_CONST.__const: 0xde8
   __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xea0
+  __DATA_CONST.__objc_selrefs: 0xeb0
   __DATA_CONST.__objc_superrefs: 0x108
   __DATA_CONST.__objc_arraydata: 0x180
   __AUTH_CONST.__auth_got: 0x780
   __AUTH_CONST.__const: 0x590
-  __AUTH_CONST.__cfstring: 0x4b80
+  __AUTH_CONST.__cfstring: 0x4bc0
   __AUTH_CONST.__objc_const: 0x4830
   __AUTH_CONST.__objc_intobj: 0x270
   __AUTH_CONST.__objc_arrayobj: 0x90

   - /System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7B705868-2102-3BC5-9BAB-958FAA2CFE3C
-  Functions: 891
-  Symbols:   3258
-  CStrings:  3366
+  UUID: C6F71B08-8847-3937-AE29-6F49EDBD215D
+  Functions: 897
+  Symbols:   3270
+  CStrings:  3384
 
Symbols:
+ -[NRDeviceManager(Internal) scrubAllDevicesWithQueue:completionBlock:]
+ -[NRDeviceManager(Internal) scrubDevice:queue:completionBlock:]
+ ___63-[NRDeviceManager(Internal) scrubDevice:queue:completionBlock:]_block_invoke
+ ___70-[NRDeviceManager(Internal) scrubAllDevicesWithQueue:completionBlock:]_block_invoke
+ ___Block_byref_object_copy_.1939
+ ___Block_byref_object_copy_.2787
+ ___Block_byref_object_dispose_.1940
+ ___Block_byref_object_dispose_.2788
+ ___block_literal_global.1958
+ ___block_literal_global.1979
+ ___block_literal_global.2764
+ ___block_literal_global.2958
+ ___block_literal_global.414
+ ___block_literal_global.518
+ ___block_literal_global.522
+ ___block_literal_global.531
+ ___block_literal_global.566
+ ___block_literal_global.78
+ ___nrCopyLogObj_block_invoke.1967
+ ___nrCopyLogObj_block_invoke.1990
+ ___nrCopyLogObj_block_invoke.2775
+ ___nrCopyLogObj_block_invoke.2939
+ _nrCopyLogObj.1970
+ _nrCopyLogObj.2183
+ _nrCopyLogObj.2767
+ _nrCopyLogObj.2932
+ _nrCopyLogObj.onceToken.1957
+ _nrCopyLogObj.onceToken.1978
+ _nrCopyLogObj.onceToken.2772
+ _nrCopyLogObj.onceToken.2936
+ _nrCopyLogObj.sNRLogObj.1959
+ _nrCopyLogObj.sNRLogObj.1980
+ _nrCopyLogObj.sNRLogObj.2773
+ _nrCopyLogObj.sNRLogObj.2937
+ _nrXPCScrubAllDevices
+ _nrXPCScrubDeviceByNRUUID
- ___Block_byref_object_copy_.1936
- ___Block_byref_object_copy_.2772
- ___Block_byref_object_dispose_.1937
- ___Block_byref_object_dispose_.2773
- ___block_literal_global.1949
- ___block_literal_global.1970
- ___block_literal_global.2749
- ___block_literal_global.2935
- ___block_literal_global.408
- ___block_literal_global.512
- ___block_literal_global.516
- ___block_literal_global.525
- ___block_literal_global.560
- ___block_literal_global.70
- ___nrCopyLogObj_block_invoke.1958
- ___nrCopyLogObj_block_invoke.1981
- ___nrCopyLogObj_block_invoke.2760
- ___nrCopyLogObj_block_invoke.2916
- _nrCopyLogObj.1961
- _nrCopyLogObj.2174
- _nrCopyLogObj.2752
- _nrCopyLogObj.2909
- _nrCopyLogObj.onceToken.1948
- _nrCopyLogObj.onceToken.1969
- _nrCopyLogObj.onceToken.2757
- _nrCopyLogObj.onceToken.2913
- _nrCopyLogObj.sNRLogObj.1950
- _nrCopyLogObj.sNRLogObj.1971
- _nrCopyLogObj.sNRLogObj.2758
- _nrCopyLogObj.sNRLogObj.2914
CStrings:
+ "%s%.30s:%-4d Failed to scrub all devices: %@"
+ "%s%.30s:%-4d Failed to scrub device %@: %@"
+ "%s%.30s:%-4d Scrubbed all devices"
+ "%s%.30s:%-4d Scrubbed device %@"
+ "%s%.30s:%-4d Scrubbing all devices"
+ "%s%.30s:%-4d Scrubbing device %@"
+ "-[NRDeviceManager(Internal) scrubAllDevicesWithQueue:completionBlock:]"
+ "-[NRDeviceManager(Internal) scrubAllDevicesWithQueue:completionBlock:]_block_invoke"
+ "-[NRDeviceManager(Internal) scrubDevice:queue:completionBlock:]"
+ "-[NRDeviceManager(Internal) scrubDevice:queue:completionBlock:]_block_invoke"
+ "ScrubAllDevices"
+ "ScrubDeviceByNRUUID"
+ "nrXPCScrubAllDevices"
+ "nrXPCScrubDeviceByNRUUID"
+ "scrubAllDevicesWithQueue:completionBlock:"
+ "scrubDevice:queue:completionBlock:"

```
