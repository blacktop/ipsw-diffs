## libarchive.2.dylib

> `/usr/lib/libarchive.2.dylib`

```diff

-138.40.4.0.0
-  __TEXT.__text: 0x72e08
-  __TEXT.__auth_stubs: 0x10a0
-  __TEXT.__const: 0x8ecc
-  __TEXT.__cstring: 0x9eeb
-  __TEXT.__unwind_info: 0x1180
-  __DATA_CONST.__got: 0x38
-  __DATA_CONST.__const: 0x1bf8
-  __AUTH_CONST.__auth_got: 0x850
+147.0.0.0.0
+  __TEXT.__text: 0xe1a64
+  __TEXT.__auth_stubs: 0x10c0
+  __TEXT.__const: 0x932c
+  __TEXT.__cstring: 0x9cb0
+  __TEXT.__unwind_info: 0xb98
+  __DATA_CONST.__got: 0x30
+  __DATA_CONST.__const: 0x1a10
+  __AUTH_CONST.__auth_got: 0x860
   __AUTH_CONST.__auth_ptr: 0x18
-  __AUTH_CONST.__const: 0x9b0
-  __DATA.__data: 0x4
-  __DATA.__bss: 0x432
-  __DATA_DIRTY.__bss: 0x270
+  __AUTH_CONST.__const: 0xd48
+  __DATA.__data: 0xc
+  __DATA.__bss: 0x1438
+  __DATA_DIRTY.__bss: 0xb4
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Security.framework/Security
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/liblzma.5.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1620
-  Symbols:   695
-  CStrings:  1762
+  Functions: 2237
+  Symbols:   2502
+  CStrings:  1825
 
Symbols:
+ <redacted>
+ ___memmove_chk
+ ___memset_chk
+ ___snprintf_chk
+ ___strcpy_chk
+ ___strncpy_chk
+ _archive_entry_filetype_is_set
+ _archive_entry_gid_is_set
+ _archive_entry_perm_is_set
+ _archive_entry_uid_is_set
+ _isalnum
+ _isdigit
+ _isprint
+ _isspace
+ _isupper
+ _strtoimax
+ _tolower
- __DefaultRuneLocale
- ___maskrune
- ___sprintf_chk
- ___tolower
- _atoi
- _memmove
- _memset_pattern16
- _snprintf
- _strcat
- _strcpy
- _strncpy
CStrings:
+ "\r\n\r\n"
+ "\x17rE8P\x90"
+ "\x1f\x8b\b"
+ " --long=%d"
+ " --threads=%d"
+ " liblz4/"
+ " libzstd/"
+ "#1/"
+ "#mtree"
+ "/\n"
+ "00"
+ "07070"
+ "070701"
+ "070702"
+ "070707"
+ "070727"
+ "1AY&SY"
+ "7z\xbc\xaf'\x1c"
+ "====\r\n"
+ "BZh"
+ "CD001"
+ "Can't allocate memory for pathname"
+ "Can't read first filter"
+ "Encrypted file is unsupported"
+ "Failed to create distance table"
+ "Failed to create literal table"
+ "Failed to create lower bits of distances table"
+ "Failed to create repeating distances table"
+ "File with multiple link targets"
+ "Internal error: Digest storage too large"
+ "Internal error: no bid/init for filter bidder"
+ "LRZI"
+ "LZIP"
+ "More than one string table exists"
+ "No support for RAR VM program filter"
+ "PK\x01\x02"
+ "PK\x03\x04"
+ "PK\x05\x06"
+ "PK\x06\x06"
+ "PK\x06\a"
+ "PK\a\b"
+ "SP\a\x01\xbe\xef"
+ "Tar size attribute is negative"
+ "Tar size attribute overflow"
+ "Truncated 7z file data"
+ "Truncated ar archive - failed consuming padding"
+ "UTF16BE"
+ "UTF16LE"
+ "UTF8"
+ "Unsupported ACL type"
+ "ZSTD codec is unsupported"
+ "__archive_read_register_bidder"
+ "`%s' compression not supported on this platform"
+ "alarm"
+ "allow"
+ "ask"
+ "audit"
+ "begin "
+ "begin-base64 "
+ "charset"
+ "comment"
+ "deny"
+ "efault"
+ "end "
+ "ftp"
+ "group@"
+ "hidden,"
+ "http"
+ "lh0"
+ "lhd"
+ "libarchive 3.7.4"
+ "mask"
+ "other"
+ "owner@"
+ "rdonly,"
+ "response"
+ "roup"
+ "ser"
+ "system,"
+ "ther"
+ "ustar "
+ "\x7fELF"
+ "\xed\xab\xee\xdb"
- "\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\r\r\r\r\r\r\r\r\x0e\x0e\x0e\x0e\x0f\x0f\x10"
- "Can't allocate memory for Pathame"
- "Invalid entry size"
- "Overflow of 64-bit file sizes"
- "Truncated ZIP end-of-file record"
- "Truncated ar archive- failed consuming padding"
- "archive_read_support_filter_bzip2"
- "archive_read_support_filter_compress"
- "archive_read_support_filter_grzip"
- "archive_read_support_filter_gzip"
- "archive_read_support_filter_lrzip"
- "archive_read_support_filter_lz4"
- "archive_read_support_filter_lzip"
- "archive_read_support_filter_lzma"
- "archive_read_support_filter_lzop"
- "archive_read_support_filter_rpm"
- "archive_read_support_filter_uu"
- "archive_read_support_filter_xz"
- "archive_read_support_filter_zstd"
- "libarchive 3.5.3"

```
