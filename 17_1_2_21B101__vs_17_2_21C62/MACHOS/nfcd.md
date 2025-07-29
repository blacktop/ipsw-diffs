## nfcd

> `/usr/libexec/nfcd`

```diff

-341.10.0.0.0
-  __TEXT.__text: 0x21867c
+342.4.1.0.0
+  __TEXT.__text: 0x2186b0
   __TEXT.__auth_stubs: 0x16d0
-  __TEXT.__objc_stubs: 0xddc0
-  __TEXT.__objc_methlist: 0x78f0
+  __TEXT.__objc_stubs: 0xdde0
+  __TEXT.__objc_methlist: 0x7900
   __TEXT.__const: 0xfc0
-  __TEXT.__oslogstring: 0x20756
-  __TEXT.__cstring: 0x29c52
+  __TEXT.__oslogstring: 0x20778
+  __TEXT.__cstring: 0x29c5f
   __TEXT.__objc_classname: 0x1782
-  __TEXT.__objc_methname: 0x15e72
+  __TEXT.__objc_methname: 0x15ea4
   __TEXT.__objc_methtype: 0x4cc9
-  __TEXT.__gcc_except_tab: 0x4784
+  __TEXT.__gcc_except_tab: 0x4700
   __TEXT.__dlopen_cstrs: 0x5ac
   __TEXT.__unwind_info: 0x305c
   __DATA_CONST.__auth_got: 0xb78
   __DATA_CONST.__got: 0x150
-  __DATA_CONST.__const: 0x6d10
-  __DATA_CONST.__cfstring: 0xf420
+  __DATA_CONST.__const: 0x6d18
+  __DATA_CONST.__cfstring: 0xf4a0
   __DATA_CONST.__objc_classlist: 0x4f0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x310
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x5a90
-  __DATA_CONST.__objc_arraydata: 0x1d88
+  __DATA_CONST.__objc_arraydata: 0x1da8
   __DATA_CONST.__objc_arrayobj: 0x3c0
-  __DATA_CONST.__objc_dictobj: 0xe60
+  __DATA_CONST.__objc_dictobj: 0xe88
   __DATA.__objc_const: 0x14930
-  __DATA.__objc_selrefs: 0x5098
+  __DATA.__objc_selrefs: 0x50a0
   __DATA.__objc_protorefs: 0x170
   __DATA.__objc_classrefs: 0x738
   __DATA.__objc_superrefs: 0x368

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libnfshared.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BFD91C85-4FEB-3A5A-BF30-BAB61E4CD5D7
-  Functions: 3984
+  UUID: 3367164A-EF73-36B8-ADF8-7AA9C63E32BA
+  Functions: 3985
   Symbols:   499
-  CStrings:  13246
+  CStrings:  13256
 
CStrings:
+ "%du"
+ "-[NFCameraStateMonitor listenForCameraNotificationFromPort:]"
+ "AppleH16CamIn"
+ "Failed to start stack; FailForward triggered"
+ "Failed to start stack; FailForward triggered (result=%{public}du)"
+ "NFAccessory Failure"
+ "NFCD built from (B&I) Stockholm_Base-342.4.1 at 21:38:29 on Nov 15 2023"
+ "[%{public}s] Cannot locate service; check hardware configuration"
+ "furyFailure:context:addlInfo:"
+ "ttrFury"
+ "writeNdefData:toTag:nLengthOptimization:error:"
- "%c[%{public}s %{public}s]:%i Contains undefined RFU bits but existing feature definition matches"
- "ACMRequirement - ACMRequirementDataRatchet"
- "NFCD built from (B&I) Stockholm_Base-341.10 at 20:16:51 on Oct 30 2023"
- "writeNdefData:toTag:error:"

```
