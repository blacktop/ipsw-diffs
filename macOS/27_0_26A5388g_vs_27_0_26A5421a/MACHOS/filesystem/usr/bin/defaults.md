## defaults

> `/usr/bin/defaults`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_selrefs`

```diff

-5027.0.63.2.0
+5027.0.69.0.0
   __TEXT.__text: 0x32b0
   __TEXT.__auth_stubs: 0x570
   __TEXT.__objc_stubs: 0x760
   __TEXT.__const: 0x48
   __TEXT.__gcc_except_tab: 0x20
-  __TEXT.__cstring: 0x10b0
+  __TEXT.__cstring: 0x10af
   __TEXT.__oslogstring: 0x3
   __TEXT.__objc_methname: 0x499
   __TEXT.__unwind_info: 0xd0
CStrings:
+ "Command line interface to a user's defaults.\nSyntax:\n\n'defaults' [-verbose] [-currentHost | -host <hostname>] [-container <container identifier>] followed by one of the following:\n\n  read                                 shows all defaults\n  read <domain>                        shows defaults for given domain\n  read <domain> <key>                  shows defaults for given domain, key\n\n  read-type <domain> <key>             shows the type for the given domain, key\n\n  write <domain> <domain_rep>          writes domain (overwrites existing)\n  write <domain> <key> <value>         writes key for domain\n\n  rename <domain> <old_key> <new_key>  renames old_key to new_key\n\n  delete <domain>                      deletes domain\n  delete <domain> <key>                deletes key in domain\n  delete-all <domain>                  deletes the domain from all containers\n  delete-all <domain> Key>             deletes key in domain from all containers\n\n  import <domain> <path to plist>      writes the plist at path to domain\n  import <domain> -                    writes a plist from stdin to domain\n  export <domain> <path to plist>      saves domain as a binary plist to path\n  export <domain> -                    writes domain as an xml plist to stdout\n  domains                              lists all domains\n  find <word>                          lists all entries containing word\n  help                                 print this help\n\n<domain> is ( <domain_name> | -app <application_name> | -globalDomain )\n         or a path to a file omitting the '.plist' extension\n\n<value> is one of:\n  <value_rep>\n  -string <string_value>\n  -data <hex_digits>\n  -int[eger] <integer_value>\n  -float  <floating-point_value>\n  -bool[ean] (true | false | yes | no)\n  -date <date_rep>\n  -array <value1> <value2> ...\n  -array-add <value1> <value2> ...\n  -dict <key1> <value1> <key2> <value2> ...\n  -dict-add <key1> <value1> ...\n"
- "Command line interface to a user's defaults.\nSyntax:\n\n'defaults' [-verbose] [-currentHost | -host <hostname>] [-container <container indentifier>] followed by one of the following:\n\n  read                                 shows all defaults\n  read <domain>                        shows defaults for given domain\n  read <domain> <key>                  shows defaults for given domain, key\n\n  read-type <domain> <key>             shows the type for the given domain, key\n\n  write <domain> <domain_rep>          writes domain (overwrites existing)\n  write <domain> <key> <value>         writes key for domain\n\n  rename <domain> <old_key> <new_key>  renames old_key to new_key\n\n  delete <domain>                      deletes domain\n  delete <domain> <key>                deletes key in domain\n  delete-all <domain>                  deletes the domain from all containers\n  delete-all <domain> Key>             deletes key in domain from all containers\n\n  import <domain> <path to plist>      writes the plist at path to domain\n  import <domain> -                    writes a plist from stdin to domain\n  export <domain> <path to plist>      saves domain as a binary plist to path\n  export <domain> -                    writes domain as an xml plist to stdout\n  domains                              lists all domains\n  find <word>                          lists all entries containing word\n  help                                 print this help\n\n<domain> is ( <domain_name> | -app <application_name> | -globalDomain )\n         or a path to a file omitting the '.plist' extension\n\n<value> is one of:\n  <value_rep>\n  -string <string_value>\n  -data <hex_digits>\n  -int[eger] <integer_value>\n  -float  <floating-point_value>\n  -bool[ean] (true | false | yes | no)\n  -date <date_rep>\n  -array <value1> <value2> ...\n  -array-add <value1> <value2> ...\n  -dict <key1> <value1> <key2> <value2> ...\n  -dict-add <key1> <value1> ...\n"
```
