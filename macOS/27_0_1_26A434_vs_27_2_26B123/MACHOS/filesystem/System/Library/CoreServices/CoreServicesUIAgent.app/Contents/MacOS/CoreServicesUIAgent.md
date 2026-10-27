## CoreServicesUIAgent

> `/System/Library/CoreServices/CoreServicesUIAgent.app/Contents/MacOS/CoreServicesUIAgent`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methtype`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_nlcatlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA.__data`

```diff

-469.0.0.0.0
-  __TEXT.__text: 0x2bc6c
+469.1.11.0.0
+  __TEXT.__text: 0x2cc50
   __TEXT.__auth_stubs: 0xed0
-  __TEXT.__objc_stubs: 0x4660
+  __TEXT.__objc_stubs: 0x4720
   __TEXT.__init_offsets: 0x8
-  __TEXT.__objc_methlist: 0x177c
+  __TEXT.__objc_methlist: 0x17f4
   __TEXT.__const: 0x128
-  __TEXT.__cstring: 0x3e51
-  __TEXT.__objc_methname: 0x4daa
-  __TEXT.__oslogstring: 0x1963
-  __TEXT.__objc_classname: 0x41d
+  __TEXT.__cstring: 0x3eb6
+  __TEXT.__objc_methname: 0x4e64
+  __TEXT.__oslogstring: 0x1b61
+  __TEXT.__objc_classname: 0x442
   __TEXT.__objc_methtype: 0x110a
-  __TEXT.__gcc_except_tab: 0x1edc
+  __TEXT.__gcc_except_tab: 0x2044
   __TEXT.__ustring: 0x16
-  __TEXT.__unwind_info: 0xf38
-  __DATA_CONST.__const: 0xfc0
-  __DATA_CONST.__cfstring: 0x4260
-  __DATA_CONST.__objc_classlist: 0xb8
+  __TEXT.__unwind_info: 0xfb8
+  __DATA_CONST.__const: 0xff0
+  __DATA_CONST.__cfstring: 0x42c0
+  __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_nlcatlist: 0x8
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x80
+  __DATA_CONST.__objc_superrefs: 0x88
   __DATA_CONST.__objc_intobj: 0xd8
   __DATA_CONST.__objc_arraydata: 0x308
   __DATA_CONST.__objc_arrayobj: 0x120
   __DATA_CONST.__objc_doubleobj: 0x30
   __DATA_CONST.__auth_got: 0x780
-  __DATA_CONST.__got: 0x600
-  __DATA.__objc_const: 0x29b0
-  __DATA.__objc_selrefs: 0x1680
-  __DATA.__objc_ivar: 0x1f4
-  __DATA.__objc_data: 0x730
+  __DATA_CONST.__got: 0x608
+  __DATA.__objc_const: 0x2a88
+  __DATA.__objc_selrefs: 0x16b0
+  __DATA.__objc_ivar: 0x1fc
+  __DATA.__objc_data: 0x780
   __DATA.__data: 0x480
   __DATA.__bss: 0x1d8
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 757
-  Symbols:   445
-  CStrings:  1889
+  Functions: 775
+  Symbols:   446
+  CStrings:  1910
 
Symbols:
+ _UTTypeInternetLocation
CStrings:
+ "%@.%@"
+ "CSUIInternetLocatorQuarantineHandler"
+ "InternetLocator"
+ "LSQInternetLocatorPath"
+ "LSQInternetLocatorTargetURL"
+ "Q_HEADLINE_INTERNET_LOCATOR"
+ "URLForApplicationToOpenURL:"
+ "_locatorURL"
+ "callerCanReachLocator"
+ "fileURLWithFileSystemRepresentation:isDirectory:relativeToURL:"
+ "internet locator quarantine: %{private}@ is not an Internet Locator file"
+ "internet locator quarantine: %{private}@ needs no approval"
+ "internet locator quarantine: caller cannot reach %{private}@"
+ "internet locator quarantine: failed to build an alert for %{private}@"
+ "internet locator quarantine: failed to set QTN_FLAG_USER_APPROVED on %{private}@"
+ "internet locator quarantine: no usable locator path in message"
+ "internet locator quarantine: user declined to open %{private}@"
+ "locatorIsInternetLocationFile"
+ "no Internet Locator headline for key %@"
+ "runApprovalAlert"
+ "targetAppName"
```
