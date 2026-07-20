## DuetActivityScheduler

> `/System/Library/PrivateFrameworks/DuetActivityScheduler.framework/Versions/A/DuetActivityScheduler`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-2467.0.14.0.0
-  __TEXT.__text: 0x3e72c
-  __TEXT.__objc_methlist: 0x4660
+2467.0.23.0.0
+  __TEXT.__text: 0x3f188
+  __TEXT.__objc_methlist: 0x46d8
   __TEXT.__const: 0x1f8
-  __TEXT.__cstring: 0x3d9a
-  __TEXT.__oslogstring: 0x2b64
-  __TEXT.__gcc_except_tab: 0x1378
-  __TEXT.__unwind_info: 0x10c0
+  __TEXT.__cstring: 0x3e4f
+  __TEXT.__oslogstring: 0x2c77
+  __TEXT.__gcc_except_tab: 0x1434
+  __TEXT.__unwind_info: 0x10d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x448
+  __DATA_CONST.__const: 0x4b0
   __DATA_CONST.__objc_classlist: 0x150
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2688
+  __DATA_CONST.__objc_selrefs: 0x26d8
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x110
   __DATA_CONST.__objc_arraydata: 0xb0
   __DATA_CONST.__got: 0x300
   __AUTH_CONST.__const: 0xea0
-  __AUTH_CONST.__cfstring: 0x4c80
-  __AUTH_CONST.__objc_const: 0x7a68
-  __AUTH_CONST.__objc_intobj: 0x210
+  __AUTH_CONST.__cfstring: 0x4ea0
+  __AUTH_CONST.__objc_const: 0x7b28
+  __AUTH_CONST.__objc_intobj: 0x228
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x690
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x444
+  __DATA.__objc_ivar: 0x454
   __DATA.__data: 0xd68
-  __DATA.__bss: 0xa8
+  __DATA.__bss: 0xb8
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x690
-  __DATA_DIRTY.__bss: 0xc8
+  __DATA_DIRTY.__bss: 0xb8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1611
-  Symbols:   3555
-  CStrings:  917
+  Functions: 1626
+  Symbols:   3573
+  CStrings:  939
 
Symbols:
+ -[_DASActivity domainPriority]
+ -[_DASActivity phase]
+ -[_DASActivity setDomainPriority:]
+ -[_DASActivity setPhase:]
+ -[_DASPlistParser domainPriorityCache]
+ -[_DASPlistParser isPhasedSchedulingActivity:]
+ -[_DASPlistParser phasedProcessingCache]
+ -[_DASPlistParser priorityForDomain:]
+ -[_DASPlistParser setDomainPriorityCache:]
+ -[_DASPlistParser setPhasedProcessingCache:]
+ OBJC_IVAR_$__DASActivity._domainPriority
+ OBJC_IVAR_$__DASActivity._phase
+ OBJC_IVAR_$__DASPlistParser._domainPriorityCache
+ OBJC_IVAR_$__DASPlistParser._phasedProcessingCache
+ _objc_msgSend$domainPriority
+ _objc_msgSend$phase
+ _objc_msgSend$setDomainPriority:
+ _objc_msgSend$setPhase:
CStrings:
+ "AIML"
+ "Can't load allowlist plist for PhasedScheduling lookup"
+ "Can't load domains plist for domain %@"
+ "Health"
+ "Mail"
+ "Media"
+ "Messages"
+ "Missing or invalid Priority key for domain %@ in domains plist"
+ "Missing or invalid domain entry for %@ in domains plist"
+ "No string mapping for domain %ld; returning sentinel priority"
+ "PhasedScheduling"
+ "Photos"
+ "Priority"
+ "Proactive"
+ "Search"
+ "SensingConnectivity"
+ "Services"
+ "Siri"
+ "StorageTech"
+ "com.apple.dasd.domains.plist"
+ "domainPriority"
+ "phase"
```
