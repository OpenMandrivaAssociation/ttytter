Name:               ttytter
Version:            2.0.01
Release:            1
Summary:            Command-Line Twitter Client
# http://www.floodgap.com/software/ttytter/dist1/%{version}.txt
Source0:            %{version}.txt.bz2
# http://www.floodgap.com/software/ffsl/license.txt
Source1:            license.txt.bz2
URL:                http://www.floodgap.com/software/ttytter/
Group:              Communications
License:            Floodgap Free Software License
Requires:           perl
Requires:           curl
Requires:           perl(Term::ReadLine)
Requires:           perl(Date::Parse)
Requires:           perl(Date::Format)
Requires:           perl(POSIX)
BuildArch:          noarch

%description
Noooo, not another Twitter client! Yes, another Twitter client. The difference
here is that you're dealing with a multi-functional, fully 100% text, Perl
command line client.

* In interactive mode, it is a fully interactive client with asynchronous
  background updates and commands. Use it over telnet, ssh or even a dummy
  terminal. Supports ANSI colour, UTF-8, hashtags and Twitter Search!
* Works within your favourite environment: modify prompt and input methods for
  many popular window and session managers, or use a compatible readline
  library. Or don't: basic editing and screen management features built-in.
* From the command line, use it to update your Twitter in shell scripts, from
  cron, and so on.
* Notification support with Growl and libnotify (and extendable to others via
  the API).
* Security: Supports Twitter OAuth and HTTP Basic Authentication, and SSL where
  supported by your user agent.
* Supports Twitter-alike APIs such as StatusNet and Identi.ca.
* Supports standard timelines and automatically fetches direct messages, and
  optionally replies/mentions, and runs queries against the Search API and
  incorporates them into your timeline as well.
* Write and use your own custom extensions!
* Run detached in -daemon mode, and make your own Twitter bot! 

%prep
%setup -q -T -c "%{name}-%{version}"
%__bzip2 -d -c "%{SOURCE0}" > "%{name}"
%__bzip2 -d -c "%{SOURCE1}" > license.txt
%__sed -i 's/\r$//' "%{name}" license.txt

%build

%install
%__install -D -m0755 "%{name}" "%{buildroot}%{_bindir}/%{name}"
%__chmod 0644 license.txt

%files
%doc license.txt
%{_bindir}/%{name}
