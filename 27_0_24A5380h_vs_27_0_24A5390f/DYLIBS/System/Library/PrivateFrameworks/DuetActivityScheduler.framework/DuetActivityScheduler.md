## DuetActivityScheduler

> `/System/Library/PrivateFrameworks/DuetActivityScheduler.framework/DuetActivityScheduler`

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

-2467.0.14.502.1
-  __TEXT.__text: 0x3e758
-  __TEXT.__objc_methlist: 0x4988
+2467.0.23.502.1
+  __TEXT.__text: 0x3f118
+  __TEXT.__objc_methlist: 0x4a00
   __TEXT.__const: 0x200
-  __TEXT.__gcc_except_tab: 0x1568
-  __TEXT.__cstring: 0x40f2
-  __TEXT.__oslogstring: 0x31da
-  __TEXT.__unwind_info: 0x12e8
+  __TEXT.__gcc_except_tab: 0x1624
+  __TEXT.__cstring: 0x41a7
+  __TEXT.__oslogstring: 0x32ed
+  __TEXT.__unwind_info: 0x1300
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xf10
+  __DATA_CONST.__const: 0xf78
   __DATA_CONST.__objc_classlist: 0x158
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x28e8
+  __DATA_CONST.__objc_selrefs: 0x2938
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x118
   __DATA_CONST.__objc_arraydata: 0x180
   __DATA_CONST.__got: 0x330
   __AUTH_CONST.__const: 0x380
-  __AUTH_CONST.__cfstring: 0x5060
-  __AUTH_CONST.__objc_const: 0x7ec8
+  __AUTH_CONST.__cfstring: 0x5280
+  __AUTH_CONST.__objc_const: 0x7f88
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__objc_intobj: 0x210
+  __AUTH_CONST.__objc_intobj: 0x228
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x6e0
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x494
+  __DATA.__objc_ivar: 0x4a4
   __DATA.__data: 0xd68
   __DATA.__bss: 0xf8
   __DATA.__common: 0x8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1674
-  Symbols:   3649
-  CStrings:  982
+  Functions: 1689
+  Symbols:   3668
+  CStrings:  1004
 
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
+ GCC_except_table13
+ _OBJC_IVAR_$__DASActivity._domainPriority
+ _OBJC_IVAR_$__DASActivity._phase
+ _OBJC_IVAR_$__DASPlistParser._domainPriorityCache
+ _OBJC_IVAR_$__DASPlistParser._phasedProcessingCache
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
