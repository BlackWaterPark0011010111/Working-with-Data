"""Task - Access nested keys
Accessing a value in a nested dictionary can lead to difficult to read syntax like: data['really']['deeply']['nested']['value'].

Implement a method get that takes a dictionary and a nested key name with levels seperated by . (really.deeply.nested.value in the example) and returns the value if it exists and None if it doesn't.

A key can also be an integer like in.a.list.0.

Input:
data = {
  'students': [
    {
      'name': 'Josephine',
      'subjects': [
        {
          'name': 'English',
          'teacher': 'Mr. Hoover'
        }
      ]
    },
    {
      'name': 'Luke',
      'subjects': [
        {
          'name': 'History',
          'teacher': 'Mrs. Peters'
        }
      ]
    },
    {
      'name': 'Julia',
      'subjects': [
        {
          'name': 'Chemistry',
          'teacher': 'Mrs. Fauci'
        }
      ]
    }
  ]
}
Output:

> get(data, 'students.1.subjects.0.name')
History

> get(data, 'students.0.subjects.0.teacher')
Mr. Hoover"""







def get(data, key_path):
    keys = key_path.split('.')  
    for key in keys:
        if isinstance(data, list):  
            try:
                key = int(key) 
            except ValueError:
                return None  
        
        if key in data if isinstance(data, dict) else key < len(data): 
            data = data[key]  
        else:
            return None  
    return data 

# Пример данных
data = {
    'students': [
        {
            'name': 'Josephine',
            'subjects': [
                {'name': 'English', 'teacher': 'Mr. Hoover'}
            ]
        },
        {
            'name': 'Luke',
            'subjects': [
                {'name': 'History', 'teacher': 'Mrs. Peters'}
            ]
        },
        {
            'name': 'Julia',
            'subjects': [
                {'name': 'Chemistry', 'teacher': 'Mrs. Fauci'}
            ]
        }
    ]
}

# Проверка работы
print(get(data, 'students.1.subjects.0.name')) 
print(get(data, 'students.0.subjects.0.teacher')) 
