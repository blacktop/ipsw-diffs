## CloudKeychainProxy

> `/System/Library/Frameworks/Security.framework/Versions/Current/Resources/CloudKeychainProxy.bundle/Contents/MacOS/CloudKeychainProxy`

### Sections with Same Size but Changed Content

- `__TEXT.__oslogstring`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__data`

```diff

-62460.0.55.0.1
-  __TEXT.__text: 0xcf4c
+62460.1.2.0.0
+  __TEXT.__text: 0xd260
   __TEXT.__auth_stubs: 0xa30
-  __TEXT.__objc_stubs: 0x1800
-  __TEXT.__objc_methlist: 0xc1c
-  __TEXT.__const: 0x108
+  __TEXT.__objc_stubs: 0x1920
+  __TEXT.__objc_methlist: 0xc54
+  __TEXT.__const: 0x100
   __TEXT.__gcc_except_tab: 0x9c
-  __TEXT.__objc_methname: 0x1ca2
-  __TEXT.__cstring: 0x89a
+  __TEXT.__objc_methname: 0x1d70
+  __TEXT.__cstring: 0x8a5
   __TEXT.__oslogstring: 0xbaf
-  __TEXT.__objc_classname: 0x150
-  __TEXT.__objc_methtype: 0x4eb
-  __TEXT.__unwind_info: 0x3d0
+  __TEXT.__objc_classname: 0x161
+  __TEXT.__objc_methtype: 0x51b
+  __TEXT.__unwind_info: 0x3e0
   __DATA_CONST.__const: 0x9b0
-  __DATA_CONST.__cfstring: 0x4a0
-  __DATA_CONST.__objc_classlist: 0x30
+  __DATA_CONST.__cfstring: 0x4e0
+  __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__auth_got: 0x528
-  __DATA_CONST.__got: 0x1c8
+  __DATA_CONST.__got: 0x1e0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x10c0
-  __DATA.__objc_selrefs: 0x850
+  __DATA.__objc_const: 0x1150
+  __DATA.__objc_selrefs: 0x8a8
   __DATA.__objc_ivar: 0xac
-  __DATA.__objc_data: 0x1e0
+  __DATA.__objc_data: 0x230
   __DATA.__data: 0x280
   __DATA.__bss: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/Versions/A/SymptomDiagnosticReporter
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 324
-  Symbols:   234
-  CStrings:  659
+  Functions: 328
+  Symbols:   237
+  CStrings:  676
 
Symbols:
+ _NSURLErrorDomain
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$_NSURLComponents
CStrings:
+ "%s Result from [Proxy requestSynchronization:]: %@"
+ "@40@0:8r*16Q24^@32"
+ "B32@0:8@16Q24"
+ "SecXPCNetworkURL"
+ "URL"
+ "allowedURLFromCString:options:error:"
+ "componentsWithString:"
+ "errorWithDomain:code:userInfo:"
+ "host"
+ "http"
+ "https"
+ "initWithUTF8String:"
+ "isAllowedURL:options:"
+ "lowercaseString"
+ "requestSynchronization:"
+ "scheme"
+ "scheme:isAllowedByOptions:"
+ "setError:code:"
+ "v32@0:8^@16q24"
- "%s Result from [Proxy waitForSynchronization:]: %@"
- "waitForSynchronization:"
```
