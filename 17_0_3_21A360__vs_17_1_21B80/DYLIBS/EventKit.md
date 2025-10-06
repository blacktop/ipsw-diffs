## EventKit

> `/System/Library/Frameworks/EventKit.framework/EventKit`

```diff

-1870.0.0.2.0
-  __TEXT.__text: 0x121c4c
+1870.1.1.3.0
+  __TEXT.__text: 0x121fc8
   __TEXT.__auth_stubs: 0x1430
-  __TEXT.__objc_methlist: 0x132c0
+  __TEXT.__objc_methlist: 0x132f8
   __TEXT.__const: 0x4f2
-  __TEXT.__cstring: 0xaabe
-  __TEXT.__oslogstring: 0xc740
+  __TEXT.__cstring: 0xaaae
+  __TEXT.__oslogstring: 0xc845
   __TEXT.__gcc_except_tab: 0x26d8
   __TEXT.__dlopen_cstrs: 0x2ba
   __TEXT.__ustring: 0x162

   __TEXT.__swift5_types: 0x14
   __TEXT.__swift5_reflstr: 0x1b2
   __TEXT.__swift5_capture: 0xa0
-  __TEXT.__unwind_info: 0x4920
+  __TEXT.__unwind_info: 0x492c
   __TEXT.__objc_classname: 0x1801
-  __TEXT.__objc_methname: 0x2abac
+  __TEXT.__objc_methname: 0x2abb2
   __TEXT.__objc_methtype: 0x3e06
-  __TEXT.__objc_stubs: 0x1e440
+  __TEXT.__objc_stubs: 0x1e3a0
   __DATA_CONST.__got: 0xbf8
-  __DATA_CONST.__const: 0x3cd8
+  __DATA_CONST.__const: 0x3cc8
   __DATA_CONST.__objc_classlist: 0x6b0
   __DATA_CONST.__objc_catlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x1a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x16808
-  __DATA_CONST.__objc_selrefs: 0x9d30
+  __DATA_CONST.__objc_const: 0x16908
+  __DATA_CONST.__objc_selrefs: 0x9d08
   __DATA_CONST.__objc_arraydata: 0x610
   __AUTH_CONST.__objc_const: 0x6338
   __AUTH_CONST.__cfstring: 0x8ec0

   __DATA.__objc_protorefs: 0x38
   __DATA.__objc_classrefs: 0xb10
   __DATA.__objc_superrefs: 0x4d0
-  __DATA.__objc_ivar: 0xc18
+  __DATA.__objc_ivar: 0xc1c
   __DATA.__data: 0x1510
   __DATA.__bss: 0x3d8
   __DATA.__common: 0x10

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: E041E9DF-065B-30A1-BB59-13370B27DEFD
-  Functions: 8179
-  Symbols:   25026
-  CStrings:  10531
+  UUID: 3E5F1020-8E89-3665-ABFB-93470158E847
+  Functions: 8187
+  Symbols:   25044
+  CStrings:  10530
 
Symbols:
+ +[EKSourceConstraints supportsSecureCoding]
+ -[EKCalendarChange .cxx_destruct]
+ -[EKCalendarChange calendarIdentifier]
+ -[EKEventStore requestAccessToEntityType:completion:].cold.1
+ -[EKEventStore requestAccessToEntityType:desiredFullAccess:testing:synchronous:reason:completion:].cold.1
+ -[EKSourceConstraints encodeWithCoder:]
+ -[EKSourceConstraints initWithCoder:]
+ -[EKSourceConstraints initWithCoder:].cold.1
+ _OBJC_IVAR_$_EKCalendarChange._calendarIdentifier
+ __OBJC_$_CLASS_PROP_LIST_EKSourceConstraints
+ __OBJC_CLASS_PROTOCOLS_$_EKSourceConstraints
+ ___block_literal_global.244
+ ___block_literal_global.382
+ ___block_literal_global.384
+ _objc_msgSend$decodeBytesForKey:returnedLength:
+ _objc_msgSend$encodeBytes:length:forKey:
- _EKInvitationNotificationsDisabledKey
- _EKSharedCalendarNotificationsDisabledKey
- ___block_literal_global.381
- ___block_literal_global.383
- _objc_msgSend$middleName
- _objc_msgSend$namePrefix
- _objc_msgSend$nameSuffix
- _objc_msgSend$nickname
- _objc_msgSend$setMiddleName:
- _objc_msgSend$setNamePrefix:
- _objc_msgSend$setNameSuffix:
CStrings:
+ "Calling request access completion handler with invalid entity type error"
+ "Calling request access completion handler with no access because this method is deprecated and the app is not a legacy app."
+ "Calling request access completion handler with result: %{BOOL}d"
+ "T@\"NSString\",R,N,V_calendarIdentifier"
+ "decodeBytesForKey:returnedLength:"
+ "encodeBytes:length:forKey:"
- "Name should not be nil."
- "middleName"
- "namePrefix"
- "nameSuffix"
- "nickname"
- "setMiddleName:"
- "setNamePrefix:"
- "setNameSuffix:"

```
