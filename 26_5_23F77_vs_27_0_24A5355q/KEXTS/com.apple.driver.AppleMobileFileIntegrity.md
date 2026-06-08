## com.apple.driver.AppleMobileFileIntegrity

> `com.apple.driver.AppleMobileFileIntegrity`

```diff

-1045.120.5.0.0
-  __TEXT.__cstring: 0xb69e
-  __TEXT.__const: 0x1538
-  __TEXT.__os_log: 0x32d
-  __TEXT_EXEC.__text: 0x283c8
+1166.0.0.0.0
+  __TEXT.__cstring: 0xb803
+  __TEXT.__const: 0x1568
+  __TEXT.__os_log: 0x3a5
+  __TEXT_EXEC.__text: 0x29a04
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x4c2
-  __DATA.__common: 0xb0
-  __DATA.__bss: 0x99
-  __DATA_CONST.__auth_got: 0x808
-  __DATA_CONST.__got: 0x158
-  __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__mod_init_func: 0x18
-  __DATA_CONST.__mod_term_func: 0x20
-  __DATA_CONST.__const: 0x40b8
+  __DATA.__data: 0x4fa
+  __DATA.__common: 0xf0
+  __DATA.__bss: 0xd1
+  __DATA_CONST.__mod_init_func: 0x20
+  __DATA_CONST.__mod_term_func: 0x28
+  __DATA_CONST.__const: 0x40a0
   __DATA_CONST.__kalloc_type: 0xf80
-  __DATA_CONST.__kalloc_var: 0x1400
+  __DATA_CONST.__kalloc_var: 0x1540
   __DATA_CONST.__assert: 0xf0
-  UUID: C872B233-CB08-31B3-BAF7-2202ED26B863
-  Functions: 900
+  __DATA_CONST.__auth_got: 0x868
+  __DATA_CONST.__got: 0xe0
+  __DATA_CONST.__auth_ptr: 0x18
+  UUID: 15F82469-3ACB-3730-B87F-F5D61D0BFC05
+  Functions: 916
   Symbols:   0
-  CStrings:  1149
+  CStrings:  1164
 
CStrings:
+ "\"AMFI cert overrun\\n\" @%s:%d"
+ "\"AMFI gave us too many certs\\n\" @%s:%d"
+ "\"AMFI: unable to create legacy CE context from monitor CE context: %u\" @%s:%d"
+ "\"AMFI: unable to get legacy context after adjustment without monitor: %u\" @%s:%d"
+ "\"AMFI: unable to obtain legacy CE context from CE context: %u\" @%s:%d"
+ "\"Bad AMFI Detached Certs size\" @%s:%d"
+ "%s: copyBytesFromInputArguments failed: %d\n"
+ "%s: failed to copy in cdhash %d\n"
+ "%s: input too large: %llu\n"
+ "%s: unexpected cd hash length: %u\n"
+ "%s: vm_allocate failed"
+ "%s: vm_map_copyin failed kr = %d"
+ "%s: vm_map_unwire failed kr = %d"
+ "%s: vm_map_wire failed kr = %d"
+ "1122211222112012122222"
+ "122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211"
+ "22:46:17"
+ "AMFI: '%s' cmsBlobInit failed: component=%#x error=%#x unique=%#x\n"
+ "AMFI: '%s' cmsBlobVerify failed: component=%#x error=%#x unique=%u\n"
+ "AMFI: '%s' cmsBlobVerifyWithAgilityHash failed: component=%#x error=%#x unique=%u\n"
+ "AMFI: '%s' cmsBlobVerifyWithAgilityHash unsupported: unique=%#x\n"
+ "AMFI: '%s' couldn't fetch certs\n"
+ "AMFI: '%s' no hash agility and first code directory is not the best one\n"
+ "AMFI: using cached detached cert data for %s\n"
+ "Bool op requires boolean parameter"
+ "CertManager.cpp"
+ "Couldn't allocate buffer for cms blob\n"
+ "Couldn't fetch detached certificates for %s\n"
+ "Couldn't find daemon.\n"
+ "Int op requires int parameter"
+ "May 27 2026"
+ "OSDetachedCertificates"
+ "PQC code signing support compiled in"
+ "String op requires string parameter"
+ "alloc_vm_buffer"
+ "cdhash-full"
+ "cryptex1.boot.rosetta"
+ "int _check_authorize_local_signing_entitlement(struct proc *)"
+ "int _check_cdhash_in_trustcache(struct proc *, user_addr_t)"
+ "iokit.OSDetachedCertificates"
+ "performCommandV3"
+ "personalized.cryptex1.update-brain"
+ "pqc_codesigning_enabled"
+ "site.ACMCredential.ACMCredentialDataPKITokenValidated"
+ "site.ACMCredential.ACMCredentialDataPKITokenValidated2"
+ "static IOReturn AppleMobileFileIntegrityUserClient::copyBytesFromInputArguments(IOExternalMethodArguments *, void **, IOByteCount *)"
+ "v16@?0r^{_OSEntitlementsReadOnly=^{OSEntitlements}{CEQueryContext={der_vm_context=^{CERuntime}{CEAccelerationContext=^{CEAccelerationElement}Q}QBB(?={ccder_read_blob=**}{?=**})}B}{_CEContext={_CEContextInfo=CI}{_CEElement={?=*Q}{?=Q{?=*Q}}}^{_CEElementIndex}Q{CEQueryContext={der_vm_context=^{CERuntime}{CEAccelerationContext=^{CEAccelerationElement}Q}QBB(?={ccder_read_blob=**}{?=**})}B}B}^{_CEContext}*{?=^{__SC_GenericBlob}}{?=BB}}8"
- "\"AMFI: '%s': Invalid first Code Directory should have been caught by xnu.\\n\" @%s:%d"
- "%s: copyTrustCacheFromInputArguments failed: %d\n"
- "112221122211201212222212"
- "12222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221"
- "20:24:38"
- "<no error obj>"
- "AMFI: '%s' does not pass CT evaluation, result: %#x\n"
- "AMFI: '%s' has unexpected digest data len %zu (type %#x)\n"
- "AMFI: '%s' has unexpected digest type, actual %#x != expected %#x\n"
- "AMFI: '%s' has unknown CT digest type %#x\n"
- "AMFI: '%s': V1 hash agility validation failed, bailing out.\n"
- "AMFI: '%s': V2 hash agility validation failed, bailing out.\n"
- "AMFI: '%s': agility data length %zu for V1 agility text is too big.\n"
- "AMFI: '%s': cannot allocate %zu bytes for V1 agility text, bailing out.\n"
- "AMFI: '%s': cannot unserialize hash agility V1 object: '%s'\n"
- "AMFI: '%s': cdhash mismatch: '%s' does not match any in V1 agility array.\n"
- "AMFI: '%s': cdhash mismatch: actual '%s' != expected '%s'\n"
- "AMFI: '%s': first code directory doesn't match the best code directory, but no hash agility data"
- "AMFI: '%s': hash agility v1 cdhashes missing or not an array, bailing out.\n"
- "AMFI: '%s': hash agility v1 data not a dictionary, bailing out.\n"
- "AMFI: '%s': no hash agility data and first cd hash type (%d) does not match best cd hash type (%d).\n"
- "Apr 23 2026"
- "cdhashes"
- "com.apple.contactsd"
- "com.apple.mediaremoted"
- "com.apple.proximitycontrold"
- "global.install-assistant"
- "performCommandV2"
- "personalized.ephemeral-cryptex"
- "personalized.trust-cache"
- "static IOReturn AppleMobileFileIntegrityUserClient::copyTrustCacheFromInputArguments(IOExternalMethodArguments *, void **, IOByteCount *)"
- "v16@?0r^{_OSEntitlementsReadOnly=^{OSEntitlements}{_CEContext={_CEContextInfo=CI}{_CEElement={?=*Q}{?=Q{?=*Q}}}^{_CEElementIndex}Q{CEQueryContext={der_vm_context=^{CERuntime}{CEAccelerationContext=^{CEAccelerationElement}Q}QBB(?={ccder_read_blob=**}{?=**})}B}B}^{_CEContext}*{?=^{__SC_GenericBlob}}{?=BB}}8"

```
