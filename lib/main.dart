import 'dart:async';
import 'dart:io';
import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:path_provider/path_provider.dart';


void main() => runApp(MyApp());

Future<String> get _localPath async{
  final directory = await getApplicationDocumentsDirectory();
  return directory.path;
}

Future<File> get _localPresentDay async{
  final path = await _localPath;
  print('/presentday.txt');
  return File('$path/presentday.json');
}

Future<File> writePresentDays(String presentdayjson) async{
  final file = await _localPresentDay;
  print(presentdayjson);
  return file.writeAsString(presentdayjson);
} 

Future<Map<String,int>> readPresentDays() async {
  try {
    final file = await _localPresentDay;

    // Read the file
    String contents = await file.readAsString();
    return json.decode(contents);
  } catch (e) {
    // If we encounter an error, return 0
    return {};
  }
}


class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(title: 'Flutter Demo Home Page'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key key, this.title}) : super(key: key);

  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class Day {
  String _day;
  List _subjects;
  Day(day,timetable){
    this._day = day;
    this._subjects = timetable;
  }
}

Map<String,List> timetable = {
  'Monday':['Linear Alg & Differential Equations',
      'Digital System Design',
      'Signals and Systems',
      'Obj Oriented Methodologies'
  ],
  'Tuesday':[
    'Calculus',
    'Obj Oriented Methodologies',
    'Linear Alg & Differential Equations',
    'Signals and Systems',
    'Digital System Design'
  ],
  'Wednesday':[
    'Comm & Discourse Strategy',
    'Signals and Systems'
  ],
  'Thursday':[
    'Digital System Design',
    'Calculus',
    'Obj Oriented Methodologies',
    'IT Workshop',
    'Comm & Discourse Strategy'
  ],
  'Friday':[
    'Signals and Systems',
    'Comm & Discourse Strategy',
    'Linear Alg & Differential Equations',
    'Obj Oriented Methodologies',
    'Calculus'
  ]
};

Map<String,int> subjectPresent = {
  'Linear Alg & Differential Equations':0,
  'Digital System Design':0,
  'Signals and Systems':0,
  'Calculus':0,
  'Comm & Discourse Strategy':0,
  'Obj Oriented Methodologies':0,
  'Sensors and Actuators':0,
  'Financial Accounting':0,
  'IT Workshop':0
};

Map<String,int> subjectTotal = {
  'Linear Alg & Differential Equations':0,
  'Digital System Design':0,
  'Signals and Systems':0,
  'Calculus':0,
  'Comm & Discourse Strategy':0,
  'Obj Oriented Methodologies':0,
  'Sensors and Actuators':0,
  'Financial Accounting':0,
  'IT Workshop':0
};

List<String> days = ["Monday","Tuesday","Wednesday",
  "Thursday", "Friday"];

class _MyHomePageState extends State<MyHomePage> {

  int _currentTab = 0;

  int currentDay = 0;

  void onTabped(int index){
    setState(() {
          _currentTab = index;
        });
    print(_currentTab);
  }

  Widget subjectpage(BuildContext context){
    return Container(
      child: ListView.builder(
        itemCount: subjectPresent.length,
        itemBuilder: (_,index){
          double perc = subjectPresent[subjectPresent.keys.toList()[index]]/subjectTotal[subjectPresent.keys.toList()[index]]*100;
          return Card(margin: EdgeInsets.all(12.0),child: Column(
                  children: [Container(
                    child:Text("${subjectPresent.keys.toList()[index]}",
                      style: TextStyle(fontSize: 20.0),
                    )
                  ),
                  Container(child: Row(
                  children:[Text("",style: TextStyle(fontSize: 15.0),),
                    Text("${subjectPresent[subjectPresent.keys.toList()[index]]}/${subjectTotal[subjectPresent.keys.toList()[index]]}",style: TextStyle(fontSize: 15.0))
                  ],
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                ),
                margin: EdgeInsets.all(12.0),
              ),
              Center(
                child: Text(
                  "$perc",
                  style: TextStyle(
                    color: perc>75?Colors.green:Colors.red
                  ),
                ),
              )
            ],
            crossAxisAlignment: CrossAxisAlignment.center,
            mainAxisAlignment: MainAxisAlignment.center,
             )
          );
        },
      ),
    );
  }

  Widget homepage(BuildContext context){
    
    var presentDay = Day(days[currentDay%5],timetable[
      days[currentDay%5]
    ]);
    return 
        Container(child:
            ListView.builder(
            itemCount: presentDay._subjects.length,
            itemBuilder: (_,index){
                return Card(margin: EdgeInsets.all(12.0),child: Column(
                  children: [Container(
                    child:Text("${presentDay._subjects[index]}",
                      style: TextStyle(fontSize: 20.0),
                    )
                  ),
                  Container(child: Row(
                  children:[Text("${presentDay._day}",style: TextStyle(fontSize: 15.0),),
                    Text("${subjectPresent[presentDay._subjects[index]]}/${subjectTotal[presentDay._subjects[index]]}",style: TextStyle(fontSize: 15.0))
                  ],
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                ),
                margin: EdgeInsets.all(12.0),
              ),
                Row(
                  children: <Widget>[Container(child:RaisedButton(
                    child: Text("Present"),
                    onPressed: (){
                      setState(() {
                        subjectPresent[presentDay._subjects[index]]++;
                        subjectTotal[presentDay._subjects[index]]++;
                      });
                      var preson = jsonEncode(subjectPresent);
                      writePresentDays(preson);
                    },
                  ),
                  margin: EdgeInsets.all(5.0),
                  ),
                  Container(child:RaisedButton(
                    child: Text("Absent"),
                    onPressed: (){
                      setState(() {
                        subjectTotal[presentDay._subjects[index]]++;
                      });
                    },
                  ),
                  margin: EdgeInsets.all(5.0),
                  )],
                  mainAxisAlignment: MainAxisAlignment.center,
                  //crossAxisAlignment: ,
                )
            ],
            crossAxisAlignment: CrossAxisAlignment.center,
            mainAxisAlignment: MainAxisAlignment.center,
             )
          );
        } )
          
    );
  }
  @override
  Widget build(BuildContext context){
    
    List<Widget> tabPages = [homepage(context),subjectpage(context)];

    return Scaffold(appBar: AppBar(
      title: Center(child:Text("Daily Attendance")),
      actions: <Widget>[
        IconButton(
          icon: Icon(Icons.navigate_next),
          onPressed: (){
            setState(() {
                          currentDay++;
                });
          },
        ),
        IconButton(
          icon: Icon(Icons.redo),
          onPressed: (){
            readPresentDays().then((value) {
                    setState(() {
                        subjectPresent = value;
                        });
                    });
          },
        )
      ],
    ),
    body: tabPages[_currentTab],
    bottomNavigationBar: BottomNavigationBar(
      currentIndex: _currentTab,
      onTap: onTabped,
      items: [
        BottomNavigationBarItem(
          icon: Icon(Icons.home),
          title: Text("Home")
        )
        ,
        BottomNavigationBarItem(
          icon: Icon(Icons.list),
          title: Text("Subjects")
        )
      ],
    )  
    );
  }
}

