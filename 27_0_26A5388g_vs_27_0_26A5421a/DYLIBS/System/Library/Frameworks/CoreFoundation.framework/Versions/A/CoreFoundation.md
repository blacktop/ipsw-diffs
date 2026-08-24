## CoreFoundation

> `/System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation`

```diff

-5027.0.63.2.0
-  __TEXT.__text: 0x2077b4
+5027.0.69.0.0
+  __TEXT.__text: 0x207f44
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x8434
   __TEXT.__const: 0x1a8114
-  __TEXT.__oslogstring: 0xb313
-  __TEXT.__cstring: 0xbbb36
-  __TEXT.__gcc_except_tab: 0x6848
+  __TEXT.__oslogstring: 0xb3a5
+  __TEXT.__cstring: 0xbbbb1
+  __TEXT.__gcc_except_tab: 0x6850
   __TEXT.__ustring: 0x1446
   __TEXT.__dlopen_cstrs: 0xcc
   __TEXT.__dof_NSAppNap: 0x4cf

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3ac740
+  __DATA_CONST.__const: 0x3ac748
   __DATA_CONST.__objc_classlist: 0x4c0
   __DATA_CONST.__objc_nlclslist: 0x58
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_nlcatlist: 0x8
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3148
+  __DATA_CONST.__objc_selrefs: 0x3150
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x328
   __DATA_CONST.__objc_arraydata: 0x1760
   __DATA_CONST.__got: 0x540
-  __AUTH_CONST.__const: 0x93a0
-  __AUTH_CONST.__cfstring: 0xd55a0
+  __AUTH_CONST.__const: 0x93c0
+  __AUTH_CONST.__cfstring: 0xd55e0
   __AUTH_CONST.__objc_const: 0xb208
   __AUTH_CONST.__const_cfobj2: 0x40
   __AUTH_CONST.__objc_dictobj: 0x848

   __DATA.__cf_except_bt: 0x2000
   __DATA.__cf_except_pack: 0x410
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x1050
+  __DATA.__bss: 0x1070
   __DATA.__common: 0xc0
   __DATA_DIRTY.__objc_data: 0x22b0
   __DATA_DIRTY.__data: 0x198

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/liboah.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 9406
-  Symbols:   14835
-  CStrings:  31431
+  Functions: 9432
+  Symbols:   14854
+  CStrings:  31436
 
Symbols:
+ CFCharacterSetCreateBitmapRepresentation
+ CFCharacterSetHasMemberInPlane
+ CFCharacterSetInitInlineBuffer
+ CFCharacterSetIsCharacterMember
+ CFCharacterSetIsLongCharacterMember
+ CFCharacterSetIsSupersetOfSet
+ _CFCharacterSetCompact
+ _CFCharacterSetFast
+ _CFCharacterSetIsInverted
+ _CFCharacterSetIsLongCharacterMemberForInline
+ _CFCharacterSetIsMutable
+ _CFCharacterSetSetIsInverted
+ __CFCharacterSetCreateCopy
+ __CFCharacterSetIsLongCharacterMemberForInline
+ __CFCharacterSetLongCharacterMemberIMPForSet.onceToken
+ __CFCharacterSetLongCharacterMemberIMPForSet.swiftIMP
+ __CFCharacterSetLongCharacterMemberIMPForSet.swiftImmortalIMP
+ _____CFCharacterSetLongCharacterMemberIMPForSet_block_invoke
+ _objc_msgSend$_fillInlineBuffer:
CStrings:
+ "Process is entitled to always include storage class."
+ "Sandbox extension creation failed: does client lack read access or entitlements to issue for path: [%{private}@] [%{private}s] [%d]"
+ "Target frontmost: n/a (issuing for pboard)"
+ "Target frontmost: n/a (issuing unrestricted)"
+ "_NSSwiftCharacterSet"
+ "com.apple.WebKit.WebContent.CaptivePortal"
+ "com.apple.private.CFPasteboard.always-include-storage-class"
- "Sandbox extension creation failed: client lacks entitlements? for path: [%{private}@] [%{private}s] [%d]"
- "Target frontmost: n/a"
```
