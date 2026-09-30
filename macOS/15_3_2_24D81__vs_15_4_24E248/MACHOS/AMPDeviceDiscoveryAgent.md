## AMPDeviceDiscoveryAgent

> `/System/Library/PrivateFrameworks/AMPDevices.framework/Versions/A/Support/AMPDeviceDiscoveryAgent`

```diff

-1.5.2.56.0
-  __TEXT.__text: 0x59b50
-  __TEXT.__auth_stubs: 0x1d60
-  __TEXT.__objc_stubs: 0x2a60
+1.5.4.70.0
+  __TEXT.__text: 0x594ec
+  __TEXT.__auth_stubs: 0x1d70
+  __TEXT.__objc_stubs: 0x2a40
   __TEXT.__init_offsets: 0x20
-  __TEXT.__objc_methlist: 0xde4
-  __TEXT.__const: 0x10e0
-  __TEXT.__cstring: 0x5c26
-  __TEXT.__oslogstring: 0x2093
-  __TEXT.__gcc_except_tab: 0x36f4
+  __TEXT.__objc_methlist: 0x11ac
+  __TEXT.__const: 0x10c8
+  __TEXT.__cstring: 0x5c12
+  __TEXT.__oslogstring: 0x20ce
+  __TEXT.__gcc_except_tab: 0x36f8
   __TEXT.__objc_classname: 0x225
-  __TEXT.__objc_methname: 0x3a80
-  __TEXT.__objc_methtype: 0xa64
-  __TEXT.__unwind_info: 0x1480
-  __DATA_CONST.__auth_got: 0xec8
-  __DATA_CONST.__got: 0x3d8
-  __DATA_CONST.__const: 0xbc0
-  __DATA_CONST.__cfstring: 0x1c20
+  __TEXT.__objc_methname: 0x3a7a
+  __TEXT.__objc_methtype: 0xa6f
+  __TEXT.__unwind_info: 0x1450
+  __DATA_CONST.__auth_got: 0xed0
+  __DATA_CONST.__got: 0x3f0
+  __DATA_CONST.__const: 0xb80
+  __DATA_CONST.__cfstring: 0x1c40
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x48
-  __DATA.__objc_const: 0x1e50
-  __DATA.__objc_selrefs: 0xdc0
+  __DATA.__objc_const: 0x1738
+  __DATA.__objc_selrefs: 0xed8
   __DATA.__objc_ivar: 0xf4
   __DATA.__objc_data: 0x410
   __DATA.__data: 0x2e0
-  __DATA.__bss: 0x4ef8
-  __DATA.__common: 0x628
+  __DATA.__bss: 0x4f28
+  __DATA.__common: 0x638
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/ApplicationServices.framework/Versions/A/ApplicationServices

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 960DCD18-4551-3136-8CA3-E4C43ACE741B
-  Functions: 1715
-  Symbols:   610
-  CStrings:  2012
+  UUID: 5F9CCA88-3935-3377-90A7-EC458F5554BF
+  Functions: 1696
+  Symbols:   612
+  CStrings:  2011
 
Symbols:
+ _AMRestorableDeviceGetChipID
+ __ZNSt3__117bad_function_callD1Ev
+ __ZTINSt3__117bad_function_callE
+ __ZTVNSt3__117bad_function_callE
+ _memset
+ _os_variant_allows_internal_security_policies
- _CFStringCreateWithBytesNoCopy
- __ZNKSt9exception4whatEv
- __ZNSt9exceptionD2Ev
- __ZTISt9exception
CStrings:
+ "((stream->magic == 'strm') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"stream->magic == 'strm'\", \"/AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/Devices/Utilities/StreamUtilities.cpp\", 21, true))"
+ "13.5.4.70"
+ "AMPErrorDomainHRESULT"
+ "B20@0:8i16"
+ "Ignoring restorable device event due to running application: %{public}@"
+ "RealityDevice"
+ "allow-vm-restore"
+ "com.apple.AMPDeviceDiscoveryAgent"
+ "ignoring restorable device event; unsupported device"
+ "info != nullptr && ((info->magic == 'srai') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"info->magic == 'srai'\", \"/AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/Devices/Utilities/StreamUtilities.cpp\", 2453, true))"
+ "info != nullptr && ((info->magic == 'srai') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"info->magic == 'srai'\", \"/AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/Devices/Utilities/StreamUtilities.cpp\", 752, true))"
+ "shouldIgnoreRestorableDeviceEvent:"
- "((stream->magic == 'strm') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"stream->magic == 'strm'\", \"/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Devices/Utilities/StreamUtilities.cpp\", 21, true))"
- "."
- ".."
- "13.5.2.56"
- "Ignoring restorable device due to running application: %{public}@"
- "VirtualMac"
- "bytes != nullptr"
- "hasPrefix:"
- "info != nullptr && ((info->magic == 'srai') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"info->magic == 'srai'\", \"/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Devices/Utilities/StreamUtilities.cpp\", 2453, true))"
- "info != nullptr && ((info->magic == 'srai') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"info->magic == 'srai'\", \"/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Devices/Utilities/StreamUtilities.cpp\", 752, true))"
- "relativeTo == nullptr"
- "shouldIgnoreRestorableDevices"
- "text != __null and uText != __null"
- "uText != nullptr"

```
