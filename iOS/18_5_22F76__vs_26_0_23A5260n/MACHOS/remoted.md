## remoted

> `/usr/libexec/remoted`

```diff

-172.100.9.0.0
-  __TEXT.__text: 0x41eb0
-  __TEXT.__auth_stubs: 0x1820
-  __TEXT.__objc_stubs: 0x2280
-  __TEXT.__objc_methlist: 0x13b8
+196.0.0.0.0
+  __TEXT.__text: 0x4356c
+  __TEXT.__auth_stubs: 0x1810
+  __TEXT.__objc_stubs: 0x23a0
+  __TEXT.__objc_methlist: 0x14a4
   __TEXT.__const: 0x1fa
-  __TEXT.__oslogstring: 0x81bc
-  __TEXT.__cstring: 0x1f61
-  __TEXT.__objc_methname: 0x22f5
-  __TEXT.__objc_classname: 0x27b
-  __TEXT.__objc_methtype: 0x6e9
-  __TEXT.__gcc_except_tab: 0x1618
-  __TEXT.__unwind_info: 0xed0
-  __DATA_CONST.__auth_got: 0xc20
+  __TEXT.__oslogstring: 0x8428
+  __TEXT.__cstring: 0x1ff7
+  __TEXT.__objc_methname: 0x23d5
+  __TEXT.__objc_classname: 0x2ce
+  __TEXT.__objc_methtype: 0x71b
+  __TEXT.__gcc_except_tab: 0x15f8
+  __TEXT.__unwind_info: 0xf00
+  __DATA_CONST.__auth_got: 0xc18
   __DATA_CONST.__got: 0x220
-  __DATA_CONST.__const: 0x12d8
-  __DATA_CONST.__cfstring: 0xd00
-  __DATA_CONST.__objc_classlist: 0xb8
+  __DATA_CONST.__const: 0x1340
+  __DATA_CONST.__cfstring: 0xd60
+  __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0xa0
-  __DATA_CONST.__objc_arraydata: 0x60
+  __DATA_CONST.__objc_superrefs: 0xb8
+  __DATA_CONST.__objc_arraydata: 0x80
   __DATA_CONST.__objc_arrayobj: 0x90
-  __DATA_CONST.__objc_intobj: 0x90
-  __DATA.__objc_const: 0x2480
-  __DATA.__objc_selrefs: 0x8d8
-  __DATA.__objc_ivar: 0x208
-  __DATA.__objc_data: 0x730
-  __DATA.__data: 0x670
-  __DATA.__bss: 0x39a
+  __DATA_CONST.__objc_intobj: 0xa8
+  __DATA_CONST.__objc_dictobj: 0x28
+  __DATA.__objc_const: 0x2668
+  __DATA.__objc_selrefs: 0x920
+  __DATA.__objc_ivar: 0x20c
+  __DATA.__objc_data: 0x820
+  __DATA.__data: 0x674
+  __DATA.__bss: 0x3e0
   __DATA.__common: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libFDR.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
-  - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 76704090-8E02-3A49-B331-887BE3D19F23
-  Functions: 1341
+  UUID: 0C579EFA-3239-33A4-8CD6-348EF43FE310
+  Functions: 1380
   Symbols:   490
-  CStrings:  1829
+  CStrings:  1868
 
Symbols:
+ _OBJC_CLASS_$_NSConstantDictionary
+ _objc_opt_respondsToSelector
- _IORegistryEntryCreateCFProperty
- _objc_retain_x28
CStrings:
+ " by default on this hardware model"
+ "%{public}@> Connect failed for %s"
+ "%{public}@> Connect succeeded for %s (client=\"%s\")"
+ "%{public}@> Skipping remote service \"%{public}s\" because backend rejected it"
+ "%{public}@> Unable to create listener for \"%s\""
+ "%{public}@> connect() failed: %{errno}d"
+ "%{public}@> connect(2) succeeded to %u"
+ "%{public}@> connectVsock completed successfully"
+ "%{public}@> connectVsock failed"
+ "%{public}@> failed to connect with %{errno}d"
+ "%{public}@> fcntl() failed: %{errno}d"
+ "%{public}@> socket() failed: %{errno}d"
+ "9uRuEueUQZFyet0P69AWMw"
+ "B24@0:8r*16"
+ "Chassis manifest is required to authenticate the BMC and is not present."
+ "Chassis manifest not required to authenticate BMC. Will skip validating that peer is in the same chassis."
+ "ExtendedSecurityDomain"
+ "Failed to read HWModelStr"
+ "NCM device is display"
+ "Not supported on virtualmachine devices"
+ "RSDLocalServiceSocketListener"
+ "RSDVirtualMachineDeviceCommon"
+ "RSDVirtualMachineHostDevice"
+ "connectToService:withTcpOption:callback:"
+ "connectVsock:"
+ "getSocketWithTcpOption:callback:"
+ "i20@0:8I16"
+ "i32@0:8*16r^{?=BBIIII}24"
+ "initHostDevice"
+ "initializing virtualmachine common"
+ "initializing virtualmachine host"
+ "j126bap"
+ "j126cap"
+ "listenVsock:port:"
+ "listenerForService:"
+ "lowercaseString"
+ "optionsForService:"
+ "remoted_fd"
+ "serviceWantsToBeExposedToDevice:"
+ "shouldExposeLocalService:"
+ "shouldExposeRemoteService:"
+ "v32@0:8r^{?=BBIIII}16@?24"
+ "virtualmachine-host-%d"
+ "virtualmachine_common"
+ "virtualmachine_device"
+ "{?=BBIIII}16@0:8"
+ "{?=BBIIII}24@0:8@16"
- " by default per EDT"
- "!"
- "%{public}s> Connect failed"
- "%{public}s> Connect succeeded (client=\"%s\")"
- "Failed to read '%s/%s' from EDT. Assuming chassis not sealed."
- "IODeviceTree:/product"
- "assertion failure: \"sa\" -> %llu"
- "fdr-sealed-chassis"
- "getSocketWithTcpOption:"
- "i24@0:8r^{?=BIIII}16"
- "i32@0:8*16r^{?=BIIII}24"
- "shouldBeExposedToDevice:"
- "{?=BIIII}16@0:8"

```
