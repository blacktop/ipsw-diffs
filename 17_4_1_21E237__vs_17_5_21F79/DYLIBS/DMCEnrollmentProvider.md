## DMCEnrollmentProvider

> `/System/Library/PrivateFrameworks/DMCEnrollmentProvider.framework/DMCEnrollmentProvider`

```diff

-3.26.5.12.0
-  __TEXT.__text: 0x3f300
+3.26.6.4.0
+  __TEXT.__text: 0x3f5b4
   __TEXT.__auth_stubs: 0x7b0
-  __TEXT.__objc_methlist: 0x5014
+  __TEXT.__objc_methlist: 0x505c
   __TEXT.__const: 0x188
   __TEXT.__oslogstring: 0x15a8
   __TEXT.__cstring: 0x2602
   __TEXT.__gcc_except_tab: 0x51c
   __TEXT.__dlopen_cstrs: 0x47
   __TEXT.__ustring: 0x50
-  __TEXT.__unwind_info: 0x1158
-  __TEXT.__objc_classname: 0x10b2
-  __TEXT.__objc_methname: 0x11dfd
-  __TEXT.__objc_methtype: 0x446d
-  __TEXT.__objc_stubs: 0xbd80
+  __TEXT.__unwind_info: 0x1160
+  __TEXT.__objc_classname: 0x10b5
+  __TEXT.__objc_methname: 0x11f41
+  __TEXT.__objc_methtype: 0x4497
+  __TEXT.__objc_stubs: 0xbe60
   __DATA_CONST.__got: 0x518
   __DATA_CONST.__const: 0xc70
   __DATA_CONST.__objc_classlist: 0x2f0
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x178
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x10680
-  __DATA_CONST.__objc_selrefs: 0x39c0
+  __DATA_CONST.__objc_const: 0x106e0
+  __DATA_CONST.__objc_selrefs: 0x3a08
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_classrefs: 0x7c8
   __DATA_CONST.__objc_superrefs: 0x250

   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__auth_got: 0x3e8
   __AUTH.__objc_data: 0x1c20
-  __DATA.__objc_ivar: 0x558
+  __DATA.__objc_ivar: 0x560
   __DATA.__data: 0x11a8
   __DATA.__bss: 0x60
   __DATA_DIRTY.__objc_data: 0x140

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1817
-  Symbols:   7268
-  CStrings:  3840
+  Functions: 1824
+  Symbols:   7291
+  CStrings:  3855
 
Symbols:
+ -[DMCEnrollmentInterface delegate]
+ -[DMCEnrollmentInterface initFromViewController:delegate:]
+ -[DMCEnrollmentInterface managedSignInButton]
+ -[DMCEnrollmentInterface setDelegate:]
+ -[DMCEnrollmentInterface setManagedSignInButton:]
+ -[DMCEnrollmentInterface setManagedSignInButtonEnabled:]
+ GCC_except_table10
+ _OBJC_IVAR_$_DMCEnrollmentInterface._delegate
+ _OBJC_IVAR_$_DMCEnrollmentInterface._managedSignInButton
+ ___58-[DMCEnrollmentInterface initFromViewController:delegate:]_block_invoke
+ _objc_msgSend$arrayWithArray:
+ _objc_msgSend$enrollmentDidBegin
+ _objc_msgSend$enrollmentDidFailWithError:
+ _objc_msgSend$enrollmentDidSucceed
+ _objc_msgSend$enrollmentWasCanceled
+ _objc_msgSend$managedSignInButton
+ _objc_msgSend$setManagedSignInButton:
- GCC_except_table2
CStrings:
+ "\x11\x15"
+ "!Q"
+ "@\"<DMCEnrollmentDelegate>\""
+ "@\"PSSpecifier\""
+ "T@\"<DMCEnrollmentDelegate>\",W,N,V_delegate"
+ "T@\"PSSpecifier\",&,N,V_managedSignInButton"
+ "_managedSignInButton"
+ "arrayWithArray:"
+ "enrollmentDidBegin"
+ "enrollmentDidFailWithError:"
+ "enrollmentDidSucceed"
+ "enrollmentWasCanceled"
+ "initFromViewController:delegate:"
+ "managedSignInButton"
+ "setManagedSignInButton:"
+ "setManagedSignInButtonEnabled:"
- "\x11\x14"

```
