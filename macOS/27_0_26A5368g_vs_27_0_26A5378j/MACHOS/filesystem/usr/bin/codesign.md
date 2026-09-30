## codesign

> `/usr/bin/codesign`

```diff

-  __TEXT.__text: 0x20fe4
-  __TEXT.__auth_stubs: 0x15d0
-  __TEXT.__objc_stubs: 0xb60
+  __TEXT.__text: 0x23c00
+  __TEXT.__auth_stubs: 0x1680
+  __TEXT.__objc_stubs: 0xcc0
   __TEXT.__init_offsets: 0xc
   __TEXT.__objc_methlist: 0x35c
-  __TEXT.__const: 0xf88
-  __TEXT.__gcc_except_tab: 0x1620
-  __TEXT.__cstring: 0x3846
-  __TEXT.__objc_methname: 0xc07
+  __TEXT.__const: 0xfa8
+  __TEXT.__gcc_except_tab: 0x1a1c
+  __TEXT.__cstring: 0x4178
+  __TEXT.__objc_methname: 0xcc7
   __TEXT.__objc_classname: 0xa0
   __TEXT.__objc_methtype: 0x1fb
   __TEXT.__constg_swiftt: 0x190

   __TEXT.__swift5_proto: 0x14
   __TEXT.__oslogstring: 0xa1
   __TEXT.__dof_security_: 0x325
-  __TEXT.__unwind_info: 0x900
+  __TEXT.__unwind_info: 0x968
   __TEXT.__eh_frame: 0x90
-  __DATA_CONST.__const: 0x1478
-  __DATA_CONST.__cfstring: 0x840
+  __DATA_CONST.__const: 0x1698
+  __DATA_CONST.__cfstring: 0x1140
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_dupclass: 0xf0
-  __DATA_CONST.__auth_got: 0xb00
-  __DATA_CONST.__got: 0x548
+  __DATA_CONST.__auth_got: 0xb58
+  __DATA_CONST.__got: 0x590
   __DATA_CONST.__auth_ptr: 0xe8
   __DATA.__objc_const: 0x528
-  __DATA.__objc_selrefs: 0x330
+  __DATA.__objc_selrefs: 0x388
   __DATA.__objc_ivar: 0x2c
   __DATA.__objc_data: 0x368
   __DATA.__data: 0x160
   __DATA.__common: 0x298
-  __DATA.__bss: 0x2a0
+  __DATA.__bss: 0x2f8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/Versions/A/CryptoKit
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/PrivateFrameworks/AppleMobileFileIntegrity.framework/Versions/A/AppleMobileFileIntegrity
   - /System/Library/PrivateFrameworks/CodesignKit.framework/Versions/A/CodesignKit
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /usr/lib/libCoreEntitlements.dylib
   - /usr/lib/libCoreEntitlements_V2.dylib
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswift_DarwinFoundation2.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 497
-  Symbols:   565
-  CStrings:  754
+  Functions: 522
+  Symbols:   584
+  CStrings:  952
 
Sections:
~ __TEXT.__init_offsets : content changed
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__dof_security_ : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_dupclass : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ _AnalyticsSendEventLazy
+ _OBJC_CLASS_$_NSBundle
+ _OBJC_CLASS_$_NSNumber
+ _SecCertificateCopyKey
+ _SecKeyCopyAttributes
+ _SecRequirementCreateWithString
+ __ZNSt3__16chrono12steady_clock3nowEv
+ ___kCFBooleanTrue
+ _dispatch_once
+ _getxattr
+ _kSecAttrKeySizeInBits
+ _kSecAttrKeyType
+ _kSecAttrKeyTypeECSECPrimeRandom
+ _kSecAttrKeyTypeRSA
+ _kSecCodeInfoPlatformIdentifier
+ _lseek
+ _malloc_type_calloc
+ _read
+ _statfs
CStrings:
+ ".app"
+ ".appex"
+ ".bundle"
+ ".dext"
+ ".dylib"
+ ".framework"
+ ".kext"
+ ".plugin"
+ ".pluginkit"
+ ".systemextension"
+ ".xctest"
+ ".xpc"
+ "/AppleInternal"
+ "/Applications"
+ "/Developer"
+ "/Downloads"
+ "/Library"
+ "/Library/Frameworks"
+ "/System"
+ "/System/Cryptexes"
+ "/System/Library"
+ "/System/Library/Caches"
+ "/System/Library/CoreServices"
+ "/System/Library/Frameworks"
+ "/System/Library/PrivateFrameworks"
+ "/Users/"
+ "/Volumes"
+ "/bin"
+ "/opt/homebrew"
+ "/private/tmp"
+ "/tmp"
+ "/usr/bin"
+ "/usr/local/Homebrew"
+ "@\"NSDictionary\"8@?0"
+ "Contents/_MASReceipt/receipt"
+ "ResourceDirectory"
+ "anchor apple"
+ "anchor apple generic and (certificate leaf[field.1.2.840.113635.100.6.1.9] or certificate leaf[field.1.2.840.113635.100.6.1.3])"
+ "anchor apple generic and certificate 1[field.1.2.840.113635.100.6.2.1] exists"
+ "anchor apple generic and certificate 1[field.1.2.840.113635.100.6.2.6] exists and (certificate leaf[field.1.2.840.113635.100.6.1.14] or certificate leaf[field.1.2.840.113635.100.6.1.13])"
+ "anchor apple generic and certificate 1[field.1.2.840.113635.100.6.2.6] exists and certificate leaf[field.1.2.840.113635.100.6.1.13] exists"
+ "arch_arm64"
+ "arch_arm64_32"
+ "arch_arm64e"
+ "arch_armv7"
+ "arch_armv7s"
+ "arch_i386"
+ "arch_unknown"
+ "arch_x86_64"
+ "architecture_count"
+ "bundlePath"
+ "bundleWithPath:"
+ "cd_hard"
+ "cd_hardened_runtime"
+ "cd_kill"
+ "cd_library_validation"
+ "cd_linker_signed"
+ "cd_restrict"
+ "com.apple.codesign.usage"
+ "com.apple.provenance"
+ "com.apple.quarantine"
+ "crypto_suite"
+ "digest_sha1"
+ "digest_sha256"
+ "digest_sha384"
+ "digest_sha512"
+ "error_code"
+ "error_has_path"
+ "error_phase"
+ "executablePath"
+ "flag_check_notarization"
+ "flag_deep"
+ "flag_detached"
+ "flag_force"
+ "flag_force_library_entitlements"
+ "flag_generate_entitlement_der"
+ "flag_has_entitlements"
+ "flag_has_runtime_version"
+ "flag_input_detached_certs"
+ "flag_launch_constraint_parent"
+ "flag_launch_constraint_responsible"
+ "flag_launch_constraint_self"
+ "flag_library_constraint"
+ "flag_library_validation"
+ "flag_opt_expires"
+ "flag_opt_hard"
+ "flag_opt_kill"
+ "flag_opt_linker_signed"
+ "flag_output_detached_certs"
+ "flag_preserve_entitlements"
+ "flag_preserve_flags"
+ "flag_preserve_identifier"
+ "flag_preserve_launch_constraints"
+ "flag_preserve_library_constraints"
+ "flag_preserve_requirements"
+ "flag_preserve_runtime"
+ "flag_remote_signing"
+ "flag_resource_rules"
+ "flag_runtime"
+ "flag_strict"
+ "flag_timestamp"
+ "has_platform_identifier"
+ "has_provenance"
+ "has_quarantine"
+ "has_timestamp"
+ "identity_type"
+ "is_app_store"
+ "is_apple_signed"
+ "is_developer_signed"
+ "is_notarized"
+ "is_remote_volume"
+ "lastPathComponent"
+ "mutableCopy"
+ "notarized"
+ "numberWithBool:"
+ "numberWithInt:"
+ "numberWithUnsignedChar:"
+ "numberWithUnsignedInt:"
+ "operation_type"
+ "path_category"
+ "rangeOfString:options:"
+ "sealed_resource_count"
+ "stringByAppendingPathComponent:"
+ "target_type"
+ "time_total_ms"
+ "v8@?0"

```
