## CoreFoundation

> `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__dof_CFRunLoop`
- `__TEXT.__dof_Cocoa_Aut`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_nlclslist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_nlcatlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__const_cfobj2`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-5027.0.59.0.0
-  __TEXT.__text: 0x1d2304
+5027.0.63.2.0
+  __TEXT.__text: 0x1d29c0
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x7b1c
   __TEXT.__const: 0x1a7d30
-  __TEXT.__oslogstring: 0x59c8
-  __TEXT.__cstring: 0x14b349
-  __TEXT.__gcc_except_tab: 0x5e20
+  __TEXT.__oslogstring: 0x59f1
+  __TEXT.__cstring: 0x14b36c
+  __TEXT.__gcc_except_tab: 0x5e18
   __TEXT.__ustring: 0x48a
   __TEXT.__dof_CFRunLoop: 0x964
   __TEXT.__dof_Cocoa_Aut: 0x652
-  __TEXT.__unwind_info: 0x6538
+  __TEXT.__unwind_info: 0x6540
   __TEXT.__eh_frame: 0x3f8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3c89b0
+  __DATA_CONST.__const: 0x3c89c0
   __DATA_CONST.__objc_classlist: 0x468
   __DATA_CONST.__objc_nlclslist: 0x58
   __DATA_CONST.__objc_catlist: 0x18

   __DATA.__cf_except_bt: 0x2000
   __DATA.__cf_except_pack: 0x410
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x894
+  __DATA.__bss: 0x85c
   __DATA.__common: 0x98
   __DATA_DIRTY.__objc_data: 0x21c0
   __DATA_DIRTY.__data: 0x148
-  __DATA_DIRTY.__bss: 0xec0
+  __DATA_DIRTY.__bss: 0xef8
   __DATA_DIRTY.__common: 0x398
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CoreServicesInternal.framework/CoreServicesInternal
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 8592
-  Symbols:   12360
-  CStrings:  44295
+  Functions: 8601
+  Symbols:   12361
+  CStrings:  44298
 
Symbols:
+ -[CFPrefsDaemon createQueueForClientWithPID:uid:]
+ -[CFPrefsDaemon createSecondaryQueueForClientWithPID:]
+ __postCFPreferencesChangedDomainsNotification
- -[CFPrefsDaemon createQueueForClientWithPID:secondary:]
- __handleExternalNotification
CStrings:
+ "/usr/bin/security"
+ "/usr/libexec/lsd"
+ "proc_pidpath(%i) error: %{darwin.errno}d"
```
