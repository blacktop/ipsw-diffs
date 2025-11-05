## securityd

> `/usr/sbin/securityd`

```diff

-61439.81.1.0.0
-  __TEXT.__text: 0x685f4
-  __TEXT.__auth_stubs: 0x1850
+61439.101.1.0.0
+  __TEXT.__text: 0x6ad3c
+  __TEXT.__auth_stubs: 0x18c0
   __TEXT.__objc_stubs: 0x220
   __TEXT.__init_offsets: 0x14
-  __TEXT.__gcc_except_tab: 0x6d68
-  __TEXT.__const: 0x251f
-  __TEXT.__cstring: 0x18da
-  __TEXT.__oslogstring: 0x3db4
+  __TEXT.__objc_methlist: 0x20
+  __TEXT.__const: 0x2507
+  __TEXT.__gcc_except_tab: 0x7d88
+  __TEXT.__cstring: 0x1bc4
+  __TEXT.__oslogstring: 0x41d9
+  __TEXT.__dlopen_cstrs: 0x66
   __TEXT.__objc_classname: 0x19
   __TEXT.__objc_methtype: 0x65
-  __TEXT.__dlopen_cstrs: 0x66
   __TEXT.__objc_methname: 0x180
   __TEXT.__dof_security_: 0x466
-  __TEXT.__unwind_info: 0x24b8
-  __DATA_CONST.__auth_got: 0xc40
-  __DATA_CONST.__got: 0x218
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x7360
-  __DATA_CONST.__cfstring: 0x260
+  __TEXT.__unwind_info: 0x2560
+  __DATA_CONST.__auth_got: 0xc78
+  __DATA_CONST.__got: 0x220
+  __DATA_CONST.__auth_ptr: 0x20
+  __DATA_CONST.__const: 0x7400
+  __DATA_CONST.__cfstring: 0x680
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA.__objc_const: 0x48
+  __DATA.__objc_const: 0x10
   __DATA.__objc_selrefs: 0x88
   __DATA.__data: 0xbc
   __DATA.__crash_info: 0x40

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libxar.1.dylib
   - /usr/lib/libz.1.dylib
-  UUID: F19D88DE-DD19-3CCC-A5D3-2393326FABAD
-  Functions: 1684
-  Symbols:   462
-  CStrings:  743
+  UUID: FE493656-4B09-346E-8685-5DFC1684DF45
+  Functions: 1698
+  Symbols:   472
+  CStrings:  833
 
Symbols:
+ _CFStringAppend
+ _CFStringAppendFormat
+ _CFStringCreateMutable
+ _CFStringCreateWithFormat
+ _SecRequirementCopyString
+ __ZNSt3__117bad_function_callD1Ev
+ __ZTINSt3__117bad_function_callE
+ __ZTVNSt3__117bad_function_callE
+ ___cxa_get_exception_ptr
+ _strlcpy
CStrings:
+ "%02x"
+ "(systemdb)user approved 'allow' for %s(%d)"
+ "(systemdb)user did not approve 'allow' for %s(%d), reason %d"
+ "(systemdb)user did not approve 'allow' for %s(%d): CssmError: %s"
+ "(systemdb)user did not approve 'allow' for %s(%d): MacOSError: %s"
+ "(systemdb)user did not approve 'allow' for %s(%d): UnixError: %s"
+ "(systemdb)user did not approve 'allow' for %s(%d): Unknown exception"
+ "<AclEntry[tag:%s]"
+ "<AclSubject[type:%d]>"
+ "<AclSubject[type:ANY]>"
+ "<AclValidationContext(action:%d)SUBJECT[%@]OBJECT[%@]>"
+ "<CodeSignatureAclSubject[legacyHash:%@][path:%s][requirement:%@]>"
+ "<CommentAclSubject>"
+ "<KeychainPromptAclSubject(flags: 0x%x, desc:%s)>"
+ "<ObjectAcl["
+ "<OriginAclSubject[slot:%d]>"
+ "<PartitionAclSubject(%@)>"
+ "<PasswordAclSubject(type:%d)>"
+ "<ProcessAclSubject(v:0x%x, m:0x%x, uid:0x%x, gid:0x%x)>"
+ "<PromptedAclSubject>"
+ "<ProtectedPasswordAclSubject>"
+ "<SimpleAclSubject(type:%d)>"
+ "<SourceAclSubject[%@]>"
+ "<SourceAclSubject[empty]>"
+ "<ThresholdAclSubject(%u of %u)"
+ ">"
+ "AUTH[%d]"
+ "AUTH[all]"
+ "AnyAclSubject"
+ "ENTRY(%s)[%@] "
+ "ENTRY(%s)[missing] "
+ "Evaluating ObjectAcl: %@"
+ "ObjectAcl REJECTS access using ACL: %@"
+ "ObjectAcl mOwner REJECTS access using ACL(exception): %@"
+ "ObjectAcl mOwner REJECTS access using ACL: %@"
+ "ObjectAcl[empty]"
+ "SUBJECT[%@]"
+ "[%@]"
+ "[null]"
+ "]>"
+ "acleval"
+ "adding XARA partition '%s' to list"
+ "approved"
+ "asking user about XARA partition for '%s'"
+ "did not approve"
+ "displaying keychain prompt for %s(%d); ACL: %@"
+ "failure extending XARA partition for '%s'"
+ "missing subject"
+ "no partition ACL - adding %s"
+ "not-init"
+ "null"
+ "rejecting prompt attempt; ACL: %@"
+ "user %s 'allow' for %s(%d)"
+ "user approved 'always allow' for %s(%d)"
+ "user approved XARA access for '%s'"
+ "user did not approve 'allow' for %s(%d), reason %d"
+ "user did not approve 'allow' for %s(%d): CssmError: %s"
+ "user did not approve 'allow' for %s(%d): MacOSError: %s"
+ "user did not approve 'allow' for %s(%d): UnixError: %s"
+ "user did not approve 'allow' for %s(%d): Unknown exception"
+ "user rejected XARA access for '%s'"
- "adding partition to list"
- "failure extending partition"
- "no partition ACL - adding"

```
