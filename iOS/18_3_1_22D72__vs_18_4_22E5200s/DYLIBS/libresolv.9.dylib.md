## libresolv.9.dylib

> `/usr/lib/libresolv.9.dylib`

```diff

-83.0.0.0.0
-  __TEXT.__text: 0x15a7c
-  __TEXT.__auth_stubs: 0x760
-  __TEXT.__const: 0x2eb
-  __TEXT.__cstring: 0x1af5
-  __TEXT.__unwind_info: 0x2f0
-  __DATA_CONST.__got: 0x30
-  __DATA_CONST.__const: 0x7c8
-  __AUTH_CONST.__auth_got: 0x3b0
+91.0.0.0.0
+  __TEXT.__text: 0x187b8
+  __TEXT.__auth_stubs: 0x820
+  __TEXT.__const: 0x403
+  __TEXT.__cstring: 0x21c7
+  __TEXT.__unwind_info: 0x330
+  __DATA_CONST.__got: 0x38
+  __DATA_CONST.__const: 0xac8
+  __AUTH_CONST.__auth_got: 0x410
   __AUTH_CONST.__auth_ptr: 0x10
-  __DATA.__data: 0x194
-  __DATA.__bss: 0x658
+  __DATA.__data: 0x1d4
+  __DATA.__bss: 0x9c0
   __DATA.__common: 0x500
+  __DATA_DIRTY.__data: 0x14
+  __DATA_DIRTY.__bss: 0x10
   - /usr/lib/libSystem.B.dylib
-  Functions: 225
-  Symbols:   342
-  CStrings:  525
+  Functions: 239
+  Symbols:   391
+  CStrings:  602
 
Symbols:
+ _CC_MD5_Final
+ _CC_MD5_Init
+ _CC_MD5_Update
+ ___assert_rtn
+ ___res_9_p_cert_syms
+ ___res_9_p_class_syms
+ ___res_9_p_key_syms
+ ___res_9_p_rcode_syms
+ ___res_9_state
+ ___strlcpy_chk
+ _clock_gettime
+ _dyld_program_minos_at_least
+ _fileno
+ _freeaddrinfo
+ _fstat
+ _getaddrinfo
+ _gmtime_r
+ _in6addr_any
+ _issetugid
+ _pselect
+ _pthread_key_create
+ _pthread_main_np
+ _pthread_once
+ _pthread_setspecific
+ _res_9_nopt_rdata
+ _res_9_nrandomid
+ _res_9_ns_name_pton2
+ _res_9_ns_name_unpack2
+ _res_9_ns_parserr2
+ _strlcpy
- ___strcpy_chk
- _getsockname
- _gmtime
- _puts
- _select
- _strcpy
- _vfprintf
CStrings:
+ "\n\t\t\t\t\t"
+ "%02X"
+ "%s:%d debugging time\n"
+ "( %u "
+ "0123456789ABCDEFGHIJKLMNOPQRSTUV=0123456789abcdefghijklmnopqrstuv"
+ "; NSID\n"
+ "; NSID: "
+ "; OPT=%u\n"
+ "; OPT=%u: "
+ ";;\t..END..\n"
+ ";;\tattempts=%d\n"
+ ";;\tdebug\n"
+ ";;\ttimeout=%d\n"
+ ";; TSIG invalid (%s)\n"
+ ";; TSIG ok\n\n"
+ ";; got answer:\n\n"
+ ";; rcode = (%s), counts = an:%d ns:%d ar:%d\n"
+ ";; res_findzonecut: FINISH n=%d (%s)\n"
+ ";; res_findzonecut: START dname='%s' class=%s, zsize=%ld, naddrs=%d\n"
+ ";; res_findzonecut: add_addrs: %d\n"
+ ";; res_findzonecut: do_query: ns_initparse failed\n"
+ ";; res_findzonecut: do_query: ns_parserr failed\n"
+ ";; res_findzonecut: do_query: res_nmkquery failed\n"
+ ";; res_findzonecut: do_query: res_nsend failed\n"
+ ";; res_findzonecut: do_query: res_nsend returned 0\n"
+ ";; res_findzonecut: get the missing glue and see if it's finally enough\n"
+ ";; res_findzonecut: get the ns rrset and see if it has enough glue\n"
+ ";; res_findzonecut: get the soa, and see if it has enough glue\n"
+ ";; res_findzonecut: get_glue: do_query('%s', %s') CNAME or DNAME found\n"
+ ";; res_findzonecut: get_glue: do_query('%s', %s') failed\n"
+ ";; res_findzonecut: get_glue: removing empty '%s' NS\n"
+ ";; res_findzonecut: get_glue: save_r('%s', %s) failed\n"
+ ";; res_findzonecut: get_ns save_ns('%s', %s) failed\n"
+ ";; res_findzonecut: get_ns: do_query('%s', %s) failed (%d)\n"
+ ";; res_findzonecut: get_soa: CNAME or DNAME found\n"
+ ";; res_findzonecut: get_soa: do_query('%s', %s) failed (%d)\n"
+ ";; res_findzonecut: get_soa: ns_name_uncompress failed\n"
+ ";; res_findzonecut: get_soa: ns_parserr(%s, %d) failed\n"
+ ";; res_findzonecut: get_soa: ns_samedomain('%s', '%s') == 0\n"
+ ";; res_findzonecut: get_soa: ns_samename() || !ns_samedomain('%s', '%s')\n"
+ ";; res_findzonecut: get_soa: out of labels\n"
+ ";; res_findzonecut: get_soa: save_ns failed\n"
+ ";; res_findzonecut: get_soa: zname(%lu) too small (%lu)\n"
+ ";; res_findzonecut: satisfy(%s): %d\n"
+ ";; res_findzonecut: save_a: malloc failed\n"
+ ";; res_findzonecut: save_a: ns_parserr(%s, %d) failed\n"
+ ";; res_findzonecut: save_ns: malloc failed\n"
+ ";; res_findzonecut: save_ns: ns_name_uncompress failed\n"
+ ";; res_findzonecut: save_ns: ns_parserr(%s, %d) failed\n"
+ ";; res_findzonecut: save_ns: save_r('%s', %s) failed\n"
+ ";; res_findzonecut: save_ns: strdup failed\n"
+ ";; res_init()... default dnsrch list:\n"
+ ";; res_nopt()\n"
+ ";; res_nopt_rdata()\n"
+ ";; res_nquery: retry without EDNS0\n"
+ ";; res_opt()... ENDS0 DNSSEC\n"
+ ";; res_query: mkquery failed\n"
+ ";; res_query: send error\n"
+ ";; res_query_mDNSResponder\n"
+ ";; server rejected TSIG (%s)\n"
+ "Algorithm obtained from OID"
+ "DH"
+ "DHCID"
+ "DLV"
+ "DNS key"
+ "DNSKEY"
+ "DNSSEC look-aside validation"
+ "DS"
+ "DSA"
+ "Diffie Hellman"
+ "Digital Signature Algorithm"
+ "EXPIREONLY"
+ "HIP"
+ "IPSEC key"
+ "IPSECKEY"
+ "IPv6 address (experminental)"
+ "NSEC"
+ "NSEC3"
+ "NSEC3 parameters"
+ "NSEC3PARAM"
+ "No algorithm"
+ "OID"
+ "OID Private"
+ "PGP"
+ "PGP certificate"
+ "PKIX"
+ "PKIX (X.509v3) Certificate"
+ "PRIVATE"
+ "RRSIG"
+ "RSA"
+ "RSA KEY with MD5 hash"
+ "SPF"
+ "SPKI"
+ "SPKI certificate"
+ "SSFP"
+ "SSH fingerprint"
+ "URL"
+ "URL Private"
+ "\\# %u%s\t; %s"
+ "__res_9_state"
+ "addlen"
+ "apl"
+ "certificate"
+ "delegation signer"
+ "dynamic host configuration identifier"
+ "host identity protocol"
+ "key exchange"
+ "len <= *buflen"
+ "naptr"
+ "nn > 0"
+ "no-nibble2"
+ "non-terminal redirection"
+ "ns_print.c"
+ "ns_sign.c"
+ "nsec"
+ "nsec3"
+ "nsid"
+ "opt"
+ "re"
+ "reload-period:"
+ "res_9_ns_sign2"
+ "rrsig"
+ "sender policy framework"
+ "unknown IPSECKEY gateway type"
- ".e.f.ip6.arpa"
- ";;\t..END.."
- ";;\tdebug"
- ";; cancelled"
- ";; res_findzonecut: "
- ";; res_init()... default dnsrch list:"
- ";; res_nopt()"
- ";; res_nquery: retry without EDNS0"
- ";; res_opt()... ENDS0 DNSSEC"
- ";; res_query: mkquery failed"
- ";; res_query: send error"
- ";; res_query_mDNSResponder"
- "FINISH n=%d (%s)"
- "START dname='%s' class=%s, zsize=%ld, naddrs=%d"
- "\\# %u (\t; %s"
- "add_addrs: %d"
- "do_query: ns_initparse failed"
- "do_query: ns_parserr failed"
- "do_query: res_nmkquery failed"
- "do_query: res_nsend failed"
- "do_query: res_nsend returned 0"
- "get the missing glue and see if it's finally enough"
- "get the ns rrset and see if it has enough glue"
- "get the soa, and see if it has enough glue"
- "get_glue: do_query('%s', %s') CNAME or DNAME found"
- "get_glue: do_query('%s', %s') failed"
- "get_glue: removing empty '%s' NS"
- "get_glue: save_r('%s', %s) failed"
- "get_ns save_ns('%s', %s) failed"
- "get_ns: do_query('%s', %s) failed (%d)"
- "get_soa: CNAME or DNAME found"
- "get_soa: do_query('%s', %s) failed (%d)"
- "get_soa: ns_name_uncompress failed"
- "get_soa: ns_parserr(%s, %d) failed"
- "get_soa: ns_samedomain('%s', '%s') == 0"
- "get_soa: ns_samename() || !ns_samedomain('%s', '%s')"
- "get_soa: out of labels"
- "get_soa: save_ns failed"
- "get_soa: zname(%zu) too small (%zu)"
- "satisfy(%s): %d"
- "save_a: malloc failed"
- "save_a: ns_parserr(%s, %d) failed"
- "save_ns: malloc failed"
- "save_ns: ns_name_uncompress failed"
- "save_ns: ns_parserr(%s, %d) failed"
- "save_ns: save_r('%s', %s) failed"
- "save_ns: strdup failed"

```
