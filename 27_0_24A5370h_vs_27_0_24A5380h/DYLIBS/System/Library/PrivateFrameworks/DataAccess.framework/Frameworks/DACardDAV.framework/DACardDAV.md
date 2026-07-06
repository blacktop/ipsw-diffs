## DACardDAV

> `/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DACardDAV.framework/DACardDAV`

```diff

-  __TEXT.__text: 0xa3c8
-  __TEXT.__objc_methlist: 0x143c
+  __TEXT.__text: 0xa9fc
+  __TEXT.__objc_methlist: 0x145c
   __TEXT.__const: 0x48
   __TEXT.__gcc_except_tab: 0x20
-  __TEXT.__cstring: 0x62b
-  __TEXT.__oslogstring: 0x6e8
-  __TEXT.__unwind_info: 0x320
+  __TEXT.__cstring: 0x637
+  __TEXT.__oslogstring: 0x72d
+  __TEXT.__unwind_info: 0x330
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x258
-  __DATA_CONST.__objc_classlist: 0x70
+  __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xee8
+  __DATA_CONST.__objc_selrefs: 0xf50
   __DATA_CONST.__objc_superrefs: 0x58
-  __DATA_CONST.__got: 0x3d0
+  __DATA_CONST.__got: 0x3e8
   __AUTH_CONST.__const: 0x100
-  __AUTH_CONST.__cfstring: 0x520
-  __AUTH_CONST.__objc_const: 0x3130
+  __AUTH_CONST.__cfstring: 0x5a0
+  __AUTH_CONST.__objc_const: 0x31c0
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x230
+  __AUTH.__objc_data: 0x280
   __DATA.__objc_ivar: 0x9c
   __DATA.__data: 0x480
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x230
   - /System/Library/Frameworks/Accounts.framework/Accounts
+  - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  Functions: 317
-  Symbols:   1478
-  CStrings:  127
+  Functions: 322
+  Symbols:   1511
+  CStrings:  136
 
Sections:
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ +[DAURLSecurity hostSharesRegistrableDomain:with:]
+ +[DAURLSecurity photoURL:isAllowedForServerHost:]
+ _DAURLSecurityIsIPLiteral
+ _DAURLSecurityNormalize
+ _DAURLSecurityRegistrableDomain
+ _NSCocoaErrorDomain
+ _OBJC_CLASS_$_DAURLSecurity
+ _OBJC_CLASS_$_NSURLComponents
+ _OBJC_METACLASS_$_DAURLSecurity
+ __CFHostGetTopLevelDomain
+ __OBJC_$_CLASS_METHODS_DAURLSecurity
+ __OBJC_CLASS_RO_$_DAURLSecurity
+ __OBJC_METACLASS_RO_$_DAURLSecurity
+ _inet_pton
+ _objc_msgSend$UTF8String
+ _objc_msgSend$componentsSeparatedByString:
+ _objc_msgSend$encodedHost
+ _objc_msgSend$hasPrefix:
+ _objc_msgSend$hasSuffix:
+ _objc_msgSend$hostSharesRegistrableDomain:with:
+ _objc_msgSend$lastObject
+ _objc_msgSend$lowercaseString
+ _objc_msgSend$photoURL:isAllowedForServerHost:
+ _objc_msgSend$stringByAppendingString:
+ _objc_msgSend$stringWithUTF8String:
+ _objc_msgSend$substringToIndex:
+ _objc_msgSend$substringWithRange:
+ _strlen
CStrings:
+ "%@.%@"
+ "."
+ "Refusing to fetch photo from %@; host does not match server host %@."
+ "["
+ "]"

```
